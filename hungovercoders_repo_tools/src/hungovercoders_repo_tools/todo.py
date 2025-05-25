import os
import re
from pathlib import Path

def get_gitignore_patterns(gitignore_path):
    patterns = []
    if not gitignore_path.exists():
        return patterns
    with gitignore_path.open() as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            patterns.append(line)
    return patterns

def is_ignored(path, patterns):
    from fnmatch import fnmatch
    # Always ignore .git/hooks/ and .git/hooks/* (githook samples)
    git_hooks_patterns = ['.git/hooks/', '.git/hooks/*']
    for gh_pattern in git_hooks_patterns:
        if fnmatch(str(path), gh_pattern) or fnmatch(str(path.relative_to(Path.cwd())), gh_pattern):
            return True
    for pattern in patterns:
        # Handle directory ignore
        if pattern.endswith('/'):
            if path.is_dir() and fnmatch(str(path.relative_to(Path.cwd())), pattern.rstrip('/')):
                return True
            if fnmatch(str(path.parent.relative_to(Path.cwd())), pattern.rstrip('/')):
                return True
        # Handle file ignore
        if fnmatch(str(path.relative_to(Path.cwd())), pattern):
            return True
    return False

def find_todos(root_dir, ignore_patterns):
    todos = []
    this_file = Path(__file__).resolve()
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Remove ignored directories in-place
        dirnames[:] = [d for d in dirnames if not is_ignored(Path(dirpath) / d, ignore_patterns)]
        for filename in filenames:
            file_path = Path(dirpath) / filename
            # Ignore this script itself
            if Path(file_path).resolve() == this_file:
                continue
            if is_ignored(file_path, ignore_patterns):
                continue
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for i, line in enumerate(f, 1):
                        match = re.search(r'TODO:(.*)', line)
                        if match:
                            todos.append((str(file_path.relative_to(root_dir)), i, match.group(1).strip()))
            except Exception:
                continue
    return todos

def write_todo_md(todos, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('# TODOs in Repository\n\n')
        f.write('| File | Line | TODO Comment |\n')
        f.write('|------|------|--------------|\n')
        if todos:
            for file, line, comment in todos:
                f.write(f'| {file} | {line} | {comment} |\n') # TODO: convert todo location to markdown link
        else:
            f.write('| _No TODOs found in tracked files (excluding .gitignore entries)._ |\n')
        f.write('\n*This list is auto-generated. Only TODOs in tracked files are shown.*\n')

def main():
    # Find the repo root by walking up until .git or .gitignore is found
    current = Path(__file__).resolve().parent
    repo_root = None
    for parent in [current] + list(current.parents):
        if (parent / '.gitignore').exists() or (parent / '.git').exists():
            repo_root = parent
            break
    if repo_root is None:
        repo_root = Path(__file__).resolve().parent.parent.parent  # fallback
    gitignore_path = repo_root / '.gitignore'
    docs_dir = repo_root / 'docs'
    docs_dir.mkdir(exist_ok=True)
    output_path = docs_dir / 'todo.md'
    ignore_patterns = get_gitignore_patterns(gitignore_path)
    todos = find_todos(repo_root, ignore_patterns)
    write_todo_md(todos, output_path)

if __name__ == '__main__':
    main()
import subprocess

def git_push(repo_path: str, commit_message: str, branch: str = "main"):
    try:
        # Stage all changes
        subprocess.run(["git", "add", "."], cwd=repo_path, check=True)
        
        # Commit changes
        subprocess.run(["git", "commit", "-m", commit_message], cwd=repo_path, check=True)
        
        # Push to origin
        subprocess.run(["git", "push", "origin", branch], cwd=repo_path, check=True)
        
        print("Changes pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")

# Example usage:
# git_push(repo_path=".", commit_message="Update via script", branch="main")

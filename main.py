
from functools import lru_cache
from ollama_package import get_llm_response

# Create a dict with git commands and discriptions

git_commands = {

                # SETUP Commands - To configure user information across all local repositories
               
                "git config --global user.name": "Set a name that is identifiable for credit when review version history",
                "git config --global user.email": "Set an email address that will be associated with each history marker",
                "git config --global color.ui auto": "set automatic command line coloring for Git for easy reviewing",
                
                # SETUP & INIT Commands - To configure user info, initalizing and cloning repositories
                
                "git init": "initialize an existing directory as a Git repository",
                "git clone": "retrieve an entire repository from a hosted location via URL",
               
               # STAGE & SNAPSHOT Commands - To work with snapshots and the Git staging area
               
                "git status": "show modified files in working directory, staged for your next commit",
                "git add": "add a file as it looks now to your next commit (stage)",
                "git reset": "unstage a file while retaining the changes in working directory",
                "git diff": "diff of what is changed but not staged",
                "git diff --staged": "diff of what is staged but not yet committed",
                "git commit -m": "commit your staged content as a new commit snapshot",
                
                # BRANCH & MERGE Commands - To isolate work in branches, change context, and integrate changes
                
                "git branch": "list your branches. a * will appear next to the currently active branch",
                "git branch [branch-name]" : "create a new branch at the current commit",
                "git checkout": "switch to another branch and check it out into your working directory",
                "git merge [branch]": "merge the specified branch’s history into the current one",
                
                # INSPECT & COMPARE Commands - To examine logs, diffs, and object information
                
                "git log" : "show all commits in the current branch’s history",
                "git log branchB..branchA" : "show the commits on branchA that are not on branchB",
                "git log --follow [file]": "show the commits that changed file, even across renames",
                "git diff branchB...branchA": "show the diff of what is in branchA that is not in branchB",
                "git show [SHA]": ":show any object in Git in human-readable format",
                
                # TRACKING PATH CHANGE Commands - To version file removes and path changes
                
                "git rm [file]": "delete the file from project and stage the removal for commit",
                "git mv [existing-path] [new-path]": "change an existing file path and stage the move",
                "git log --stat -M": "show all commit logs with indication of any paths that moved",
                
                # IGNORE PATTERN Commands - To prevent unintentional staging or commiting of files
                
                "logs/*.notes pattern*/": "Save a file with desired patterns as .gitignore with either direct string matches or wildcard globs.",
                "git config --global core.excludesfile [file]": "system wide ignore pattern for all local repositories",
                
                # SHARE & UPDATE Commands - To retrieve updates from another repo and update local repos
                
                "git remote add [alias] [url]": "add a git URL as an alias",
                "git fetch [alias]": "fetch down all the branches from that Git remote",
                "git merge [alias]/[branch]": "merge a remote branch into your current branch to bring it up to date",
                "git push [alias] [branch]": "Transmit local branch commits to the remote repository branch",
                "git pull": "fetch and merge any commits from the tracking remote branch",
                
                # REWRITING HISTORY Commands - To rewrite branches, update commits, and clear history
                
                "git rebase [branch]": "apply any commits of current branch ahead of specified one",
                "git reset --hard [commit]": "clear staging area, rewrite working tree from specified commit",
                
                # TEMPORARY COMMITS Commands - To temporarily store modified, tracked files in order to change branches
                
                "git stash": "Save modified and staged changes",
                "git stash list" : "list stack-order of stashed file changes",
                "git stash pop": "write working from top of stash stack",
                "git stash drop": "discard the changes from top of stash stack"

}


def get_user_query() -> str: 
    user_query = input("Please describe the git command that you need: ")
    return user_query

def get_git_command(user_query: str) -> str:
    max_attempts = 3
    for _ in range(max_attempts):
        llm_command = get_llm_response(user_query).strip()
        print(f"LLM returned: '{llm_command}'")
        if llm_command in git_commands:
            return (
            f"The best matching Git Command is: {llm_command}\n"
            f"Description: {git_commands[llm_command]}\n")
    return "Sorry, I couldn't find a matching Git command. Please try rephrasing your request."
        

def main(): 
    # The main function for the CLI

    print(f"""
Welcome to Git-Ai! This program uses a simple AI Model
to help you find the right Git command based on your description.""")
    
    print("Go ahead and ask it any Git command related questions! When you're finished, type exit to stop the program")

    while True: 
        user_query = get_user_query()

        if user_query.lower() == "exit":
            print("Thank you for using Git-Ai! Goodbye :)")
            break

        git_command = get_git_command(user_query)
        print(git_command)

if __name__ == "__main__":
    main()
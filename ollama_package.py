import ollama
from functools import lru_cache

@lru_cache(maxsize=128)
def get_llm_response(user_query: str) -> str:

# Initialize the ollama API client
    client = ollama.Client()
    model = "phi3"
    prompt = f"""
    You are an expert system that matches plain English descriptions of Git commands to actual Git commands.
    Given this user request: "{user_query}", reply with the singular, exact git command from the list below that best matches the request.
    Do NOT include any explanation, description, or extra text. If no match is found, reply with an empty string ("").


    Available commands:
    git config --global user.name
    git config --global user.email
    git config --global color.ui auto
    git init
    git clone
    git status
    git add
    git reset
    git diff
    git diff --staged
    git commit -m
    git branch
    git branch [branch-name]
    git checkout
    git merge [branch]
    git log
    git log branchB..branchA
    git log --follow [file]
    git diff branchB...branchA
    git show [SHA]
    git rm [file] 
    git mv [existing-path] [new-path]
    git log --stat -M
    logs/*.notes pattern*/ 
    git config --global core.excludesfile [file] 
    git remote add [alias] [url] 
    git fetch [alias]
    git merge [alias]/[branch]
    git push [alias] [branch]
    git pull
    git rebase [branch]
    git reset --hard [commit]
    git stash
    git stash list
    git stash pop
    git stash drop

    """

# Send the query to the model

    response = client.generate(model=model, prompt=prompt)

# Return the llm response
    return response['response']


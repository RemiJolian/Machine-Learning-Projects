# Git Workflow Best Practices

## Table of Contents

- [Git Workflow Best Practices](#git-workflow-best-practices)
  - [Table of Contents](#table-of-contents)
  - [Branch Strategy](#branch-strategy)
    - [Workflow](#workflow)
    - [Feature Branch Naming Convention](#feature-branch-naming-convention)
  - [Commit Best Practices](#commit-best-practices)
  - [Pull Requests](#pull-requests)
  - [Code Review](#code-review)
  - [Merging](#merging)
  - [Release Management](#release-management)
  - [Git Commands and Tips](#git-commands-and-tips)

## Branch Strategy

We follow a modified Git Flow strategy:

- `main`: The main branch where the source code always reflects a production-ready state.
- `dev`: The branch where features are integrated for the next release.
- `feature/*`: Feature branches for ongoing development work.
- `hotfix/*`: Hotfix branches for critical bugs in production.
- `release/*`: Release branches for finalizing a new production release.

### Workflow

1. Create a new feature branch from `dev`:

   ```
   git checkout dev
   git pull origin dev
   git checkout -b feature/your-feature-name
   ```

2. Regularly push your feature branch to the remote repository:

   ```
   git push -u origin feature/your-feature-name
   ```

3. When the feature is complete, create a pull request to merge into `dev`.

### Feature Branch Naming Convention

1. Use the prefix "feature/".
2. Use kebab-case (lowercase with hyphens).
3. Be descriptive but concise (2-4 words).
4. Include ticket number if applicable.
5. Avoid uppercase letters and special characters.

Example format:

```
feature/building-field-boundary
```

Examples:

```
feature/user-authentication
feature/Clickup-Sprint03-interactive-map
feature/implement-role-access-functionality
```

## Commit Best Practices

- Make small, focused commits that encompass a single logical change.
- Write clear, concise commit messages:
  - Use the imperative mood in the subject line (e.g., "Add feature" not "Added feature").
  - Limit the subject line to 50 characters.
  - Provide more detailed explanations in the commit body, if necessary.
  - Reference issue numbers in the commit message when applicable.

Example:

```
Add user authentication feature

- Implement login functionality
- Add session management
- Create user registration form

Closes #123
```

- Avoid committing sensitive information (passwords, API keys, etc.).
- Commit often to make reviews easier and enable more granular reverts if needed.

## Pull Requests

- Create a pull request when you're ready to merge your feature into `dev`.
- Use a clear and descriptive title for the pull request.
- Provide a detailed description of the changes, the motivation behind them, and any potential side effects.
- Reference related issues in the pull request description.
- Assign relevant team members as reviewers.
- Include any necessary documentation updates.
- Ensure all CI checks pass before requesting a review.

## Code Review

- Reviewers should focus on:
  - Code correctness
  - Test coverage
  - Code style and standards adherence
  - Potential bugs or edge cases
  - Performance implications
- Be constructive and respectful in code review comments.
- Use "Request changes" for critical issues and "Approve" when satisfied with the changes.
- The author should address all comments and reach a resolution.

## Merging

- Use "Squash and merge" for feature branches to keep the main branch history clean.
- Delete the feature branch after merging.
- Ensure the pull request has been approved by at least one reviewer before merging.
- Avoid merging your own pull requests; seek a review from a team member.

## Release Management

1. Create a `release/x.y.z` branch from `dev` when ready to release.
2. Make any final adjustments and version bumps in this branch.
3. Merge the release branch into both `main` and `dev`.
4. Tag the release commit in `main` with the version number.
5. Delete the release branch after merging.

## Git Commands and Tips

- Regularly update your local branches:

  ```
  git fetch --all
  git pull origin dev
  ```

- Rebase your feature branch onto the latest `dev`:

  ```
  git checkout feature/your-feature
  git rebase dev
  ```

- Squash commits before merging:

  ```
  git rebase -i HEAD~<number of commits>
  ```

- Use `git stash` to temporarily store uncommitted changes.

- Utilize `git log --graph --oneline --all` for a visual representation of the branch history.

Remember, this workflow is a guideline. Adapt it as necessary to fit your team's specific needs and project requirements.

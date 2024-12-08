# Backend Design Strategy: IE Bank CI/CD Implementation

---

## Table of Contents

1. [Git Feature Branch Strategy](#git-feature-branch-strategy)
2. [Continuous Integration Workflow](#continuous-integration-workflow)
3. [References](#references)

---

## Git Feature Branch Strategy

### Overview

The backend development process follows a Git Feature Branch strategy to ensure reliable development and smooth deployments. Key aspects include:

- **Branching Strategy**: Developers use short-lived branches for new features, bug fixes, or CI/CD updates.
- **Pull Requests**: Changes are merged into the `main` branch only after a thorough code review.
- **Branch Protection Rules**:
  - Require pull request approvals before merging.
  - Require status checks to pass CI tests.
- **Deployment Workflow**:
  - Pushes to feature branches trigger deployment to the **Development** environment.
  - Pull requests to the `main` branch trigger deployment to **Development** and **UAT** environments.
  - Pushes to the `main` branch trigger deployment to **Development**, **UAT**, and **Production** environments.

### GitHub Configuration

1. **Branch Protection Rules**:
   - Navigate to `Settings > Branches > Branch Protection Rules`.
   - Add a rule for the `main` branch:
     - Require pull request reviews and passing checks.

2. **Feature Branch Workflow**:
   - Create branches with the following conventions:
     - Features: `feature/<description>`
     - Bug fixes: `bugfix/<description>`
     - CI/CD updates: `ci-cd-rework`
   - Merge branches into `main` only after passing all CI checks and reviews.

---

## Continuous Integration Workflow

### Overview

The backend CI workflow automates the build, linting, testing, and deployment of the Python application. It ensures robust, high-quality releases across environments.

### Build Steps

1. **Set Up Python**:
   - Configures Python version `3.11` using the `actions/setup-python@v5` action.
   - **Purpose**: Ensures consistent Python environments for all builds.

2. **Upgrade Pip**:
   - Runs `python -m pip install --upgrade pip`.
   - **Purpose**: Ensures the latest version of Pip for dependency management.

3. **Install Dependencies**:
   - Installs required dependencies from `requirements.txt`.
   - **Purpose**: Prepares the application for linting and testing.

4. **Lint Code**:
   - Installs and runs `flake8` to enforce Python coding standards.
   - **Purpose**: Ensures clean, maintainable code.

5. **Run Tests**:
   - Executes `pytest` to validate functionality and generate test coverage.
   - **Purpose**: Verifies application correctness and reliability.

6. **Upload Artifact**:
   - Uses `actions/upload-artifact@v4` to store build artifacts for deployment.
   - **Purpose**: Ensures consistency between build and deployment steps.

### Workflow Triggers

- Triggered by pushes to the `ci-cd-rework` branch.
- Triggered by pull requests to the `main` branch.
- Manually triggered via workflow dispatch.

---

## References

- [DevOps Checklist - Azure Architecture Center | Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/checklist/dev-ops)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Azure Web Apps Deploy Action](https://github.com/Azure/webapps-deploy)

# 🚀 Sharbo App

## 📖 Table of Contents
- [Introduction](#introduction)
- [Branching Strategy](#branching-strategy)
- [Workflow](#workflow)
- [CI/CD Pipeline](#cicd-pipeline)
- [Testing Strategy](#testing-strategy)
- [Deployment](#deployment)
- [Contributing](#contributing)

## Introduction

Welcome to the Sharbo App repository! This document outlines our development process, branching strategy, and CI/CD pipeline. Our goal is to maintain high code quality, ensure smooth collaboration, and facilitate reliable deployments.

## Branching Strategy

We use a modified GitFlow workflow with the following branches:

- `main`: Production-ready code
- `staging`: Pre-production testing
- `development`: Integration branch for features and fixes
- `feature/*`: For new features
- `fix/*`: For bug fixes

## Workflow

1. **Feature/Fix Development**
   - Create a new branch from `development`:
     ```
     git checkout development
     git pull origin development
     git checkout -b feature/your-feature-name
     ```
   - Develop and test your changes locally
   - Push your branch and create a Pull Request (PR) to `development`

2. **Code Review**
   - At least one team member must review and approve the PR
   - Address any comments and make necessary changes

3. **Merge to Development**
   - Once approved, merge the PR into `development`
   - The development CI/CD pipeline will run

4. **Staging**
   - Periodically, create a PR from `development` to `staging`
   - Run thorough QA tests on the staging environment
   - Fix any issues by creating new `fix/*` branches

5. **Production Release**
   - When staging is stable, create a PR from `staging` to `main`
   - After final approval, merge to deploy to production

## CI/CD Pipeline

We use GitHub Actions for our CI/CD pipeline. Each stage has its own workflow:

### Feature/Fix Branches
- Triggered on push to `feature/*` and `fix/*` branches
- Runs linter and ~unit tests~
- Verifies Docker build

### Development
- Triggered on push to `development` and PRs to `development`
- Runs unit and integration tests
- Builds and stores Docker image as an artifact

### Staging
- Triggered on push to `staging`
- Runs all tests (unit, integration, ~E2E~)
- Builds and pushes Docker image to ECR
- Deploys to staging Lambda function

### Production
- Triggered on push to `main`
- Runs all tests (unit, integration, ~E2E~)
- Builds and pushes Docker image to ECR
- Deploys to production Lambda function
- Creates a GitHub release (For SDK)

## Testing Strategy

We employ a comprehensive testing strategy to ensure code quality and reliability:

1. **Linting Tests**
    - code pushed to feature/fix branches adheres to coding standards and guidelines
    - Runs as part of the CI pipeline triggered by commits to feature/fix branches
    -  Immediate feedback to developers

2. **Unit Tests**
   - Test individual components in isolation
   - Run in development, staging, and production workflows
   - Fast feedback for developers

3. **Integration Tests**
   - Test interactions between components
   - Run in development, staging, and production workflows
   - Ensure different parts of the application work together

4. **End-to-End (E2E) Tests** (POSTMAN integration/Frontend Logic)
   - Test entire application flow
   - Run in staging and production workflows
   - Validate the application from a user's perspective

5. **Manual QA**
   - Performed on the staging environment
   - Catch issues that automated tests might miss
   - Validate user experience and business logic

## Deployment

We use AWS services for deployment:

- **Amazon ECR**: Stores our Docker images
- **AWS Lambda**: Hosts our application
- **GitHub Actions**: Automates our deployment process

Deployments are automated for staging and production environments, triggered by merges to the respective branches.

## Contributing

1. Fork the repository
3. Create your feature branch (`git checkout -b feature/AmazingFeature`)
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

Please ensure you've run tests locally before pushing your changes.

---

By following this workflow, we ensure:

- 🛠️ Consistent development practices across the team
- 🧪 Thorough testing at each stage of development
- 🚀 Smooth and reliable deployments
- 🔍 Early detection of issues through our CI/CD pipeline
- 🤝 Collaborative development through code reviews

Remember, this process is designed to maintain high code quality and smooth operations. If you have any questions or suggestions for improvement, please don't hesitate to reach out to @Abhijith14 .

Happy coding! 🎉

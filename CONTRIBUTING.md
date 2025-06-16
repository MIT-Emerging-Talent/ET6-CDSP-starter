# Contributing to DataCents

Thank you for your interest in contributing to DataCents! This document provides
guidelines and instructions for contributing to our project.

## 🎯 Project Focus

DataCents is focused on predicting over-indebtedness risk among Gen Z Buy Now,
Pay Later (BNPL) users. We welcome contributions that help us achieve this goal.

## 🤝 How to Contribute

### 1. Fork and Clone

- Fork the repository
- Clone your fork locally
- Set up the development environment:

  ```bash
  conda env create -f environment.yml
  conda activate datacents
  ```

### 2. Branching

- Create a new branch for your feature/fix:

  ```bash
  git checkout -b feature/your-feature-name
  ```

- Use descriptive branch names that reflect the purpose of your changes

### 3. Development Guidelines

#### Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Include docstrings for all functions and classes
- Keep functions focused and single-purpose

#### Data Analysis

- Document all data preprocessing steps
- Include clear explanations of feature engineering
- Provide visualizations where appropriate
- Comment on statistical significance of findings

#### Machine Learning

- Document model selection rationale
- Include performance metrics and evaluation methods
- Provide clear explanations of feature importance
- Document hyperparameter tuning process

### 4. Documentation

- Update README.md if your changes affect project setup or usage
- Document new features or changes in the appropriate section
- Include examples where helpful
- Update requirements.txt if adding new dependencies

### 5. Testing

- Write tests for new functionality
- Ensure all tests pass before submitting
- Include edge cases in your tests
- Document test coverage

### 6. Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the documentation with any new dependencies
3. The PR will be merged once you have the sign-off of at least one other developer

## 📝 Pull Request Template

```markdown
## Description
[Describe your changes here]

## Related Issue
[Link to the issue this PR addresses]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement
- [ ] Test addition/update

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented my code where needed
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective
- [ ] All tests pass

## Additional Notes
[Any additional information that might be helpful]
```

## 🚫 Code of Conduct

- Be respectful and inclusive
- Be patient and welcoming
- Be thoughtful
- Be collaborative
- When disagreeing, try to understand why

## 📚 Resources

- [Python Documentation](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Git Documentation](https://git-scm.com/doc)

## 🤔 Questions?

If you have any questions, please:

1. Check the existing documentation
2. Search through existing issues
3. Create a new issue if needed

Thank you for contributing to DataCents! 🚀

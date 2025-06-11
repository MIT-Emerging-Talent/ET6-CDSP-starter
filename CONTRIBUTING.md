# Contributing to Our Finance Data Science Project

Welcome to our collaborative finance data science repository! This guide will help you contribute effectively to our quantitative analysis project while maintaining code quality and following best practices.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Pull Request Process](#pull-request-process)
- [Code Quality and Standards](#code-quality-and-standards)
- [Documentation Guidelines](#documentation-guidelines)
- [Issue Management](#issue-management)
- [Project Board Management](#project-board-management)
- [Handling Conflicts](#handling-conflicts)
- [Best Practices](#best-practices)

## Getting Started

### Clone vs Fork Decision

**When to Clone (Recommended for Team Members):**

- You're already a collaborator on the repository
- Working on regular features, bug fixes, or analysis tasks
- Need direct access to push branches and create PRs

**When to Fork:**

- You're making major architectural changes that need extensive discussion
- Experimenting with significant new features that might not be accepted
- You're an external contributor without direct repository access
- Working on a personal version or derivative of the project

### Cloning the Repository

```bash
# Clone the repository
git clone https://github.com/nyangweso-rodgers/finance-analysis.git
cd finance-analysis

# Set up your local environment
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Create your development branch
git checkout -b feature/portfolio-optimization
```

### Forking the Repository (If Needed)

1. Click the "Fork" button on the repository page
2. Clone your fork locally:

```bash
git clone https://github.com/[your-username]/finance-analysis.git
cd finance-analysis

# Add upstream remote
git remote add upstream https://github.com/nyangweso-rodgers/finance-analysis.git
```

## Development Workflow

### Branch Naming Conventions

- `feature/portfolio-analysis` - New portfolio optimization features
- `feature/crypto-tracker` - Cryptocurrency analysis tools
- `feature/risk-metrics` - Risk assessment calculations
- `bugfix/sharpe-ratio-calculation` - Bug fixes for financial metrics
- `hotfix/data-feed-connection` - Critical fixes for data sources
- `docs/trading-strategy-guide` - Documentation updates
- `refactor/backtesting-engine` - Code refactoring
- `analysis/tech-stock-performance` - Market analysis work

### Making Changes

1. **Always start from the latest main branch:**

```bash
git checkout main
git pull origin main
git checkout -b feature/your-new-feature
```

2. **Make your changes** following our coding standards
3. **Test your changes** thoroughly
4. **Commit with descriptive messages:**

```bash
git add .
git commit -m "Add cryptocurrency portfolio tracker with real-time pricing

- Implement Binance API integration for live prices
- Add portfolio rebalancing alerts for BTC/ETH holdings
- Update documentation for crypto trading functions"
```

## Pull Request Process

### Creating a Pull Request

1. **Push your branch:**

```bash
git push origin feature/your-feature-name
```

2. **Create PR on GitHub:**
   - Navigate to the repository
   - Click "New Pull Request"
   - Select your branch as the source
   - Fill out the PR template (`.github/PULL_REQUEST_TEMPLATE.md`) completely

### PR Template Requirements

Your PR should include:

```markdown
## Description
Brief description of changes and motivation

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Financial analysis
- [ ] Documentation update
- [ ] Refactoring

## Testing
- [ ] Tested locally
- [ ] Added/updated tests
- [ ] Verified backtesting functionality
- [ ] Validated against historical data

## Linked Issues
Closes #123
Related to #456
```

### Linking Issues to PRs

- **Closing issues:** Use keywords like `Closes #123`, `Fixes #123`, or `Resolves #123`
- **Referencing issues:** Use `Related to #123` or `Addresses #123`
- **Multiple issues:** `Closes #123, Fixes #456`

### Assigning Reviewers

1. **Assign yourself** to the PR in the "Assignees" section
2. **Request reviewers** from team members with relevant expertise:
   - Quantitative analysis changes → quant team members
   - Trading strategy changes → experienced traders
   - Risk management changes → risk assessment specialists
   - Infrastructure changes → technical lead
   - Documentation → anyone familiar with the topic
3. **Minimum review requirement:** At least one approval required due to branch protection

### Linking to Project Board

1. Navigate to the "Projects" tab on your PR
2. Add the PR to the appropriate project board
3. Move the associated issue to "In Review" column
4. Update status as the PR progresses

## Code Quality and Standards

### Automated Checks - "ET CI Checks"

Our repository runs a comprehensive quality control suite called **"ET CI Checks"** on every push and pull request. Think of it as your personal code quality guardian that never sleeps! Here's what happens behind the scenes:

**🔍 File Structure Detective (`ls_linting`):**

- Scans your entire project structure to ensure files follow naming conventions
- Catches inconsistent naming patterns that could confuse team members
- Runs on Ubuntu's lightning-fast servers

**📝 Markdown Style Police (`md_formatting`):**

- Uses `markdownlint` with our custom configuration (`.markdownlint.yml`)
- Ensures all documentation looks professional and consistent
- Checks for proper heading hierarchy, link formatting, and spacing

**🐍 Python Code Formatter (`py_formatting`):**

- Leverages the blazing-fast `ruff` formatter to check code style
- Ensures consistent formatting across all Python files
- Fails fast if code doesn't meet our formatting standards

**🔧 Python Linting Duo (`py_linting`):**

- **Primary Guardian:** `ruff` performs comprehensive linting (MUST PASS)
- **Advisory Mentor:** `pylint` provides additional insights (warnings only)
- If pylint finds issues, it creates warnings for discussion during code review
- Automatically ignores virtual environments and cache directories

**🧪 Smart Test Runner (`py_tests`):**

- Intelligently searches for test files matching `**/test_*.py` pattern
- Only runs tests if test files are actually found
- Uses Python's built-in unittest framework
- Provides clear feedback about test discovery and execution

**📓 Jupyter Notebook Quality Guard (`py_notebook_linting`):**

- Uses `nbqa` to run `pylint` on Jupyter notebooks
- Ensures your analysis notebooks maintain code quality standards
- Provides warnings for notebook-specific issues to discuss in reviews

All checks run in parallel for maximum efficiency, and the system is smart enough to continue running other checks even if one fails, giving you a complete picture of your code quality.

### Fixing Linting Errors

**Python issues:**

```bash
# Format code with ruff (fast and comprehensive)
ruff format .

# Check for linting issues
ruff check .

# Auto-fix many issues
ruff check --fix .
```

**Markdown issues:**

```bash
# Fix common markdown issues
markdownlint --fix **/*.md
```

**Jupyter Notebook issues:**

```bash
# Install nbqa if not already installed
pip install nbqa

# Format notebooks
nbqa ruff format *.ipynb
```

### Pre-commit Hooks (Recommended)

Install pre-commit hooks to catch issues early:

```bash
pip install pre-commit
pre-commit install
```

## Documentation Guidelines

### Multi-Level Documentation Strategy

Comprehensive documentation is crucial for financial analysis projects. Follow this hierarchy:

#### 1. Module-Level Documentation

Every Python module should start with a detailed docstring:

```python
"""
Portfolio optimization and risk analysis utilities.

This module provides comprehensive tools for modern portfolio theory implementation,
including mean-variance optimization, risk parity strategies, and performance
attribution analysis. Suitable for both individual investors and institutional
portfolio management.

Key Features:
    - Markowitz efficient frontier calculation
    - Black-Litterman model implementation
    - VaR and CVaR risk metrics
    - Sharpe ratio and alpha/beta calculations

Dependencies:
    - numpy: Numerical computations
    - pandas: Data manipulation
    - scipy: Optimization algorithms
    - yfinance: Market data retrieval

Example:
    >>> from portfolio_optimizer import calculate_efficient_frontier
    >>> weights = calculate_efficient_frontier(returns_df, target_return=0.12)
    >>> print(f"Optimal weights: {weights}")

Author: Your Name
Created: 2025-06-11
Last Modified: 2025-06-11
Version: 1.0.0
"""
```

#### 2. Class-Level Documentation

For financial models and data structures:

```python
class TradingStrategy:
    """
    Base class for implementing quantitative trading strategies.
    
    This class provides the framework for backtesting and live trading
    of systematic investment strategies. It handles position sizing,
    risk management, and performance tracking.
    
    Attributes:
        initial_capital (float): Starting capital for backtesting
        risk_per_trade (float): Maximum risk per trade as percentage
        positions (Dict[str, Position]): Current portfolio positions
        performance_metrics (Dict[str, float]): Strategy performance stats
        
    Methods:
        generate_signals(): Abstract method for signal generation
        execute_trades(): Execute trades based on signals
        calculate_performance(): Compute strategy performance metrics
        
    Example:
        >>> strategy = MeanReversionStrategy(initial_capital=100000)
        >>> strategy.backtest(start_date='2023-01-01', end_date='2024-01-01')
        >>> print(strategy.performance_metrics['sharpe_ratio'])
    """
```

#### 3. Function-Level Documentation

Detailed docstrings for all functions:

```python
def calculate_portfolio_var(
    returns: pd.DataFrame, 
    weights: np.ndarray, 
    confidence_level: float = 0.95,
    method: str = 'historical'
) -> float:
    """
    Calculate Value at Risk (VaR) for a portfolio using specified method.
    
    VaR represents the maximum expected loss over a given time period
    at a specified confidence level. This function supports multiple
    calculation methods for robust risk assessment.
    
    Args:
        returns: DataFrame with daily returns for each asset
            Shape: (n_days, n_assets)
            Index: DatetimeIndex with trading dates
            Columns: Asset symbols (e.g., 'AAPL', 'MSFT')
        weights: Portfolio weights for each asset
            Shape: (n_assets,)
            Must sum to 1.0
        confidence_level: Confidence level for VaR calculation
            Typical values: 0.90, 0.95, 0.99
            Default: 0.95 (95% confidence)
        method: Calculation method
            Options: 'historical', 'parametric', 'monte_carlo'
            Default: 'historical'
            
    Returns:
        Value at Risk as a positive number representing potential loss
        Units: Same as returns (typically decimal, e.g., 0.05 = 5%)
        
    Raises:
        ValueError: If weights don't sum to 1.0 or confidence_level not in (0,1)
        KeyError: If returns DataFrame is empty or contains NaN values
        
    Example:
        >>> returns = pd.DataFrame({
        ...     'AAPL': [0.01, -0.02, 0.015, -0.01],
        ...     'MSFT': [0.005, -0.01, 0.02, 0.01]
        ... })
        >>> weights = np.array([0.6, 0.4])
        >>> var_95 = calculate_portfolio_var(returns, weights, 0.95)
        >>> print(f"95% VaR: {var_95:.2%}")
        95% VaR: 2.34%
        
    Note:
        - Historical method uses empirical distribution of returns
        - Parametric method assumes normal distribution
        - Monte Carlo uses simulation for complex portfolios
        
    References:
        - Jorion, P. (2006). Value at Risk: The New Benchmark for Managing Financial Risk
        - RiskMetrics Technical Document (1996)
    """
```

#### 4. Inline Documentation

Strategic comments within functions:

```python
def backtest_momentum_strategy(prices_df, lookback_period=20, holding_period=5):
    """Backtest a momentum trading strategy on historical price data."""
    
    # Calculate momentum signals using price rate of change
    # ROC = (Current Price - Price N periods ago) / Price N periods ago
    momentum_signals = prices_df.pct_change(periods=lookback_period)
    
    # Generate trading signals: buy top quartile, sell bottom quartile
    # This approach follows Jegadeesh and Titman (1993) momentum research
    buy_threshold = momentum_signals.quantile(0.75, axis=1)
    sell_threshold = momentum_signals.quantile(0.25, axis=1)
    
    # Create position matrix: 1 for long, -1 for short, 0 for neutral
    positions = pd.DataFrame(0, index=prices_df.index, columns=prices_df.columns)
    
    for date in momentum_signals.index:
        # Long positions: momentum above 75th percentile
        long_mask = momentum_signals.loc[date] > buy_threshold[date]
        positions.loc[date, long_mask] = 1
        
        # Short positions: momentum below 25th percentile  
        short_mask = momentum_signals.loc[date] < sell_threshold[date]
        positions.loc[date, short_mask] = -1
    
    # Calculate forward returns for the holding period
    # Shift positions to avoid look-ahead bias
    forward_returns = prices_df.pct_change(holding_period).shift(-holding_period)
    
    # Portfolio returns = sum of (position * forward_return * equal_weight)
    equal_weight = 1 / len(prices_df.columns)
    portfolio_returns = (positions * forward_returns * equal_weight).sum(axis=1)
    
    return portfolio_returns.dropna()
```

#### 5. Jupyter Notebook Documentation

Structure your analysis notebooks with clear narrative:

```markdown
# Cryptocurrency Portfolio Analysis: Risk-Return Optimization

## Executive Summary
This analysis evaluates a cryptocurrency portfolio using modern portfolio theory
to optimize risk-adjusted returns for a $50,000 investment across major digital assets.

## Methodology
- **Universe**: Top 10 cryptocurrencies by market cap
- **Period**: 2023-01-01 to 2024-12-31
- **Rebalancing**: Monthly
- **Risk Model**: Historical volatility with 252-day rolling window

## Key Findings
- Optimal portfolio achieves 2.1 Sharpe ratio vs 1.3 for equal-weight
- Maximum drawdown reduced from 45% to 28% through diversification
- Bitcoin allocation optimal at 40% for risk-averse investors
```

### Documentation Files Structure

```
docs/
├── README.md                    # Project overview and quick start
├── CONTRIBUTING.md             # This file
├── api/
│   ├── portfolio_optimizer.md  # API documentation for modules
│   └── risk_metrics.md
├── tutorials/
│   ├── getting_started.md      # Beginner tutorials
│   ├── advanced_strategies.md  # Complex trading strategies
│   └── backtesting_guide.md    # How to backtest strategies
├── examples/
│   ├── portfolio_optimization.ipynb
│   ├── crypto_analysis.ipynb
│   └── options_strategies.ipynb
└── references/
    ├── financial_formulas.md   # Mathematical references
    └── data_sources.md         # Data provider information
```

## Issue Management

### Creating Issues

1. **Use descriptive titles:** "Add cryptocurrency momentum trading strategy"
2. **Provide context:** Background, expected behavior, current behavior
3. **Add labels:** Use repository labels for categorization
4. **Assign appropriate team members**
5. **Link to project board**

### Common Labels

- `bug` - Something isn't working (e.g., backtesting errors)
- `enhancement` - New feature or request (e.g., new trading indicators)
- `documentation` - Improvements or additions to docs
- `analysis` - Market analysis and research tasks
- `trading-strategy` - New trading algorithm implementations
- `risk-management` - Risk assessment and control features
- `data-source` - Market data integration issues
- `performance` - Speed and efficiency improvements
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention needed
- `priority: high` - Urgent items (e.g., live trading bugs)

### Adding Labels

1. Navigate to the issue
2. Click "Labels" in the right sidebar
3. Select appropriate labels
4. Create new labels if needed via repository settings

## Project Board Management

### Board Columns

- **TODO:** New issues prioritized and ready to start
- **DOING:** Currently being worked on (assign yourself)
- **READY FOR REVIEW:** Pull requests created and awaiting review
- **REVIEWING:** Pull requests currently under active review
- **NEEDS REVISION:** Pull requests requiring changes before merge
- **DONE:** Completed and merged work

### Moving Cards

1. **Creating issue → TODO**
2. **Starting work → DOING** (assign yourself)
3. **Creating PR → READY FOR REVIEW**
4. **Reviewer assigned → REVIEWING**
5. **Changes requested → NEEDS REVISION**
6. **Addressing feedback → REVIEWING** (after updates)
7. **Merging PR → DONE**

## Handling Conflicts

### Git Conflicts

1. **Fetch latest changes:**

```bash
git fetch origin main
git rebase origin/main
```

2. **Resolve conflicts manually:**
   - Open conflicted files
   - Look for conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
   - Keep the correct version
   - Remove conflict markers

3. **Test and commit:**

```bash
git add .
git rebase --continue
git push --force-with-lease origin feature/your-branch
```

### Merge Conflicts in PRs

1. **Sync your branch:**

```bash
git checkout main
git pull origin main
git checkout feature/your-branch
git merge main
```

2. **Resolve conflicts and push:**

```bash
# Resolve conflicts
git add .
git commit -m "Resolve merge conflicts with main"
git push origin feature/your-branch
```

## Best Practices

### Code Organization

- Keep functions focused and single-purpose
- Use meaningful variable names
- Separate data processing from analysis
- Create reusable utility functions
- Maintain consistent coding style

### Data Science Specific

- **Version your data:** Use DVC or similar tools for large datasets
- **Document data sources:** Include origin, date, preprocessing steps, and API endpoints
- **Reproducible analysis:** Set random seeds, save environment specs (`requirements.txt`)
- **Clear visualizations:** Always include titles, labels, and financial context
- **Validate assumptions:** Test data quality and statistical assumptions
- **Backtest responsibly:** Use proper train/validation/test splits, avoid look-ahead bias
- **Risk disclosure:** Document assumptions, limitations, and potential risks in analysis

### Finance-Specific Best Practices

- **Market data integrity:** Always validate data for splits, dividends, and survivorship bias
- **Time zones:** Be explicit about market hours and time zones (NYSE, NASDAQ, etc.)
- **Transaction costs:** Include realistic trading costs in backtests
- **Risk management:** Implement position sizing and stop-loss mechanisms
- **Regulatory compliance:** Ensure analysis complies with relevant financial regulations
- **Performance attribution:** Clearly separate alpha from beta in strategy analysis

### Collaboration

- **Communicate early:** Discuss major changes before implementing
- **Small, focused PRs:** Easier to review and less likely to conflict
- **Regular updates:** Keep issues and PRs updated with progress
- **Code reviews:** Provide constructive feedback and ask questions
- **Documentation:** Update docs as you change code

### Security and Privacy

- **Never commit sensitive data:** Use `.gitignore` for data files, API keys, trading credentials
- **Environment variables:** Store secrets in `.env` files (never commit these!)
- **Data anonymization:** Remove or mask PII in shared datasets
- **Access controls:** Respect data usage agreements and API rate limits
- **Trading security:** Never commit live trading API keys or account credentialsasets
- **Access controls:** Respect data usage agreements and permissions

## Getting Help

- **Slack/Teams:** Quick questions and discussions
- **GitHub Issues:** Bug reports and feature requests
- **Code Review:** Detailed feedback on implementation
- **Team Meetings:** Weekly sync on project progress

Remember: Good collaboration makes everyone's work better. Don't hesitate to ask questions, suggest improvements, and help your teammates succeed!

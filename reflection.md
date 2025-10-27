1. Which issues were the easiest to fix, and which were the hardest? Why?
Easiest:
The easiest fixes were the stylistic ones — such as removing unused imports, correcting variable naming to follow PEP 8 (e.g., ItemCount → item_count), and adding missing docstrings. These didn’t affect how the program worked, so they were quick cleanups that improved readability and consistency.
Hardest:
The hardest fixes were related to security and logic, especially replacing eval(input()) with safe input handling and refactoring the main loop to handle invalid inputs gracefully. It required adding input validation functions, exception handling, and modifying how user input was processed without breaking the flow of the program. Setting up proper logging instead of print() statements also took effort, as every print call had to be replaced with the appropriate log level (info, error, warning).

2. Did the static analysis tools report any false positives? If so, describe one example.
Yes — Pylint flagged a few low-severity warnings like “missing docstring” for short helper functions and “too-few-public-methods” for simple classes such as InventoryItem.
These weren’t actual issues in the program’s logic or security. However, I still resolved them by adding short docstrings to keep the code consistent and improve documentation quality.

3. How would you integrate static analysis tools into your actual software development workflow?
I would integrate Pylint, Flake8, and Bandit into the development workflow as follows:
Continuous Integration (CI): Configure GitHub Actions to automatically run these tools on every commit or pull request, ensuring that no new errors are introduced.
Pre-commit Hooks: Use pre-commit to run linting and security checks locally before code is committed.
Regular Reviews: Review linting reports as part of code reviews to maintain readability, structure, and security throughout the project.
This way, issues like unsafe input handling, poor exception usage, or inconsistent formatting can be caught early before deployment.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

After applying the fixes:
The code became much more structured, readable, and maintainable.
Replacing print() with the logging module added professionalism and flexibility for debugging.
Security improved by removing eval(), adding input validation, and replacing bare exceptions with specific ones.
Using constants instead of hard-coded numbers made the code cleaner and easier to modify.
Adding docstrings and type hints improved clarity and long-term maintainability.
Overall, the refactored version is safer, cleaner, and PEP 8 compliant — it’s now suitable for production-level standards.
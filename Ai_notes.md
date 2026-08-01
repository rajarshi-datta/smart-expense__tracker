## AI Tool Used

- ChatGPT

## 1. Which parts were AI-generated vs. written by me

### AI Assisted With
- Suggested the initial FastAPI project structure.
- Provided guidance on designing REST API endpoints.
- Suggested Pydantic model structure.
- Suggested pytest test cases.
- Helped prepare the README format.

### Implemented by Me
- Created the project structure and files.
- Set up the virtual environment and installed dependencies.
- Implemented the API endpoints in FastAPI.
- Implemented JSON file storage.
- Fixed import errors and module path issues.
- Corrected JSON serialization issues for date objects.
- Tested every endpoint using Swagger UI.
- Ran pytest and fixed issues until all tests passed.
- Prepared the project for GitHub submission.

## 2. What I validated, tested, or changed

- Changed imports to relative imports.
- Fixed JSON file path handling.
- Fixed serialization of Python date objects using `model_dump(mode="json")`.
- Added proper error handling for deleting non-existent expenses.
- Verified all endpoints manually using Swagger UI.
- Executed automated tests using pytest.

## 3. AI suggestions not used

- Did not use SQLite because the assignment allowed JSON storage.
- Did not implement Docker because I selected OpenAPI/Swagger documentation as the optional bonus.
- Kept the project simple and focused only on the required functionality.
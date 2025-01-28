 1. Clone the Repository
Before making any changes, clone the repository to your local machine:

git clone https://github.com/profmanjupriya/PyBootcampHW.git
cd PyBootcampHW

2. Create and Switch to Your Own Branch
Each student should create a new branch using their lastname_firstname to avoid conflicts:

git checkout -b lastname_firstname

Example: If your name is John Doe, you can create a branch like this:
git checkout -b doe_john

 3. Add Your Work
Place your work inside the submissions/ folder.
Name your file yourname_hw.py (e.g., john_doe_hw.py).
Example command to add your file:

cp my_solution.py submissions/john_doe_hw.py
git add submissions/john_doe_hw.py
git commit -m "Added my homework submission"


4. Push Your Branch to GitHub
Push your branch to the repository:

git push origin lastname_firstname

Example:
git push origin doe_john

5. Create a Pull Request
After pushing your branch:

Go to the repository on GitHub.
Click Compare & Pull Request next to your branch.
Make sure the PR is set to merge into main.
Add a short description and submit the Pull Request (PR).

6. Wait for Review
Your instructor will review your submission.
If changes are needed, update your branch and push again:

git add submissions/john_doe_hw.py
git commit -m "Updated my submission"
git push origin doe_john

Once approved, your PR will be merged into the main branch.

Important Notes
✔ Only modify your own file inside the submissions/ folder.
✔ Do not modify other students’ files or the repository structure.
✔ Always work in your branch—do not push directly to main.
✔ If unsure, ask for help before pushing! 🚀

Happy coding! 🎉🚀
Instructor: Prof. Manju Priya



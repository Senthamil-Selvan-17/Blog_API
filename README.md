# Blog API

An API-only backend using DRF that handles blogs, comments, and users. Instead of serving HTML pages, API will return JSON data that a frontend could use.
## 🚀Features
- **User Management**
  - Allows user to signup and login.
Implemented authentication(JWT tokens) which verifies the users.
- **Blog Posts** 
  - Users can create blog posts and posts belong to a specific user.
Anyone can view single post and all posts. Only the author can edit or delete their own post.
- **Comments** 
  - Users can comment on blog posts. Each comment belongs to a specific post and a specific user. Users can delete their own comments.
Show all comments under a post.
- **Permissions**  
  - Anyone can view posts & comments.
Only the authenticated users can create posts and write comments.
Only the owners can edit/delete their own posts & comments

## Learnings
  - Based on our needs, we can customize the inherited classes and its methods

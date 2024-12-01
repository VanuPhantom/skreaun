# Skreaun
*Skreaun* is my personal blogging engine built with Django.

## Features
- [x] A list of blog posts
- [x] Rendering of blog posts with Markdown
- [x] Sorting blog posts by date
- [x] Pagination
- [x] A home page
- [x] Displaying recent blog posts on the landing page
- [x] A management UI for adding blog posts
- [x] Tests
- [x] A custom 404 page
- [x] CI
- [x] Infrastructure provisioning using Terraform
- [ ] Deploying the app using Docker

## Terraform and Linode
*Skreaun* uses [*Terraform*](https://terraform.io) to deploy its infrastructure on [Linode](https://linode.com).
This requires you to provide a **Linode personal access token**. This token should be put in `infrastructure/linode-token.txt`.

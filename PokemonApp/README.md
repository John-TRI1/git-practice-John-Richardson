# Pokémon Card Storage Web App

## Overview
This project is a Pokémon Card Storage Web App that allows users to view, manage, and submit Pokémon cards, as well as assemble decks. Admins have additional privileges to approve and manage submitted cards, decks, and users.

---

## Features
### User Roles:
- **Users:**
  - View all Pokémon cards.
  - Submit new cards (pending admin approval).
  - Assemble and manage decks (add/remove cards).

- **Admins:**
  - Approve user-submitted cards.
  - Add new cards.
  - Modify and delete existing cards.
  - Manage users, decks, and cards.

---

## Entity-Relationship Diagram (ERD)

Below is the ERD diagram that represents the database structure for the Pokémon Card Storage Web App.


```mermaid

erDiagram
    USER {
        int UserID PK
        string Name
        string Email
    }

    ADMIN {
        int AdminID PK
        string Name
        string Email
        string Permissions
    }

    DECK {
        int DeckID PK
        string DeckName
        int UserID FK
    }

    CARD {
        int CardID PK
        string Name
        string Type
        string Rarity
        int Attack
        int Defense
        int DeckID FK
    }

    %% Relationships
    USER ||--o{ DECK : "owns"
    DECK ||--o{ CARD : "contains"
    ADMIN ||--o{ USER : "manages"
    ADMIN ||--o{ DECK : "manages"
    ADMIN ||--o{ CARD : "manages and approves"
    USER ||..o{ CARD : "submits for approval"

```

## User Flow Diagram

This diagram represents how users and admins interact with the Pokémon Card Storage Web App. It includes the following key interactions:
- **Users**: View cards, submit cards for approval, and manage decks.
- **Admins**: Approve cards, manage users, decks, and cards.

Below is the user flow diagram:

```mermaid
flowchart TD
    %% Start of Flow
    Start["Start: User Logs In"] --> UserDecision{"Is the user an Admin or Regular User?"}

    %% User Path
    UserDecision -- "Regular User" --> ViewCards["View Pokémon Cards"]
    ViewCards --> UserAction{"What action does the user want to perform?"}

    %% User Path: Create Deck
    UserAction -- "Create a Deck" --> AddCards["Select Cards for the Deck"]
    AddCards --> MoreCards{"Add More Cards?"}
    MoreCards -- "Yes" --> AddCards
    MoreCards -- "No" --> CompleteDeck["Deck Successfully Created"]
    CompleteDeck --> EndUser["End of User Path"]

    %% User Path: Submit a Card
    UserAction -- "Submit a New Card" --> SubmitCard["Submit New Card for Approval"]
    SubmitCard --> CardPending["Card Pending Admin Approval"]
    CardPending --> EndUser

    %% Admin Path
    UserDecision -- "Admin" --> ReviewSubmissions["Review Submitted Cards"]
    ReviewSubmissions --> AdminApproval{"Approve or Reject the Card?"}

    %% Admin Decision Outcomes
    AdminApproval -- "Approve" --> NotifyApproval["Notify User: Card Approved"]
    NotifyApproval --> EndAdmin["End of Admin Path"]
    AdminApproval -- "Reject" --> NotifyRejection["Notify User: Card Rejected"]
    NotifyRejection --> EndAdmin

    %% Admin Additional Actions
    ReviewSubmissions --> ManageAdminTasks{"Perform Admin Tasks?"}
    ManageAdminTasks -- "Manage Users" --> ManageUsers["Add/Edit/Delete Users"]
    ManageAdminTasks -- "Manage Decks" --> ManageDecks["Add/Edit/Delete Decks"]
    ManageAdminTasks -- "Manage Cards" --> ManageCards["Add/Edit/Delete Cards"]
    ManageUsers --> EndAdmin
    ManageDecks --> EndAdmin
    ManageCards --> EndAdmin

```
## System Architecture Diagram

This diagram illustrates the architecture of the Pokémon Card Storage Web App, highlighting the interactions between users, the frontend, backend, API endpoints, and the database. It ensures a clear understanding of how data flows and roles are managed within the system. Key components and interactions include:

- **Regular Users**:
  - View Pokémon cards.
  - Create decks by selecting cards.
  - Submit new cards for admin approval.

- **Admins**:
  - Review and approve or reject card submissions.
  - Manage users, decks, and Pokémon cards (add, edit, delete).

- **Frontend (User Interface)**:
  - The primary point of interaction for users and admins, handling inputs and displaying responses.

- **API Endpoints**:
  - Bridge the communication between the frontend and backend, ensuring secure and efficient data exchange.

- **Backend (Business Logic)**:
  - Implements the core functionality of the app, processing requests and enforcing rules.

- **Database**:
  - Stores all application data, including user accounts, card details, deck compositions, and submission statuses.

Below is the system architecture diagram:

```mermaid

graph TD
    %% Define Users
    RegularUser["Regular User"]
    AdminUser["Admin User"]

    %% User Actions
    RegularUser --> |"View Cards"| Frontend
    RegularUser --> |"Create Decks"| Frontend
    RegularUser --> |"Submit Cards"| Frontend
    AdminUser --> |"Review Submissions"| Frontend
    AdminUser --> |"Manage Users"| Frontend
    AdminUser --> |"Manage Decks"| Frontend
    AdminUser --> |"Manage Cards"| Frontend

    %% Frontend to API
    Frontend["Frontend (User Interface)"] --> |"Send Requests"| API
    API["API Endpoints"] --> |"Query/Update"| Backend
    Backend["Backend (Business Logic)"] --> |"Query/Update"| Database
    Database["Database"] --> |"Return Data"| Backend
    Backend --> |"Return Data"| API
    API --> |"Return Responses"| Frontend

```

## API Endpoints Table

This table lists the key API endpoints for the Pokémon Card Storage Web App. It includes the HTTP methods, descriptions, and authentication/authorization requirements.

| Endpoint               | HTTP Method | Description                               | Authentication Required | Authorization Level   |
|------------------------|-------------|-------------------------------------------|--------------------------|-----------------------|
| `/api/cards`           | GET         | Fetch all Pokémon cards.                 | Yes                      | Regular User/Admin    |
| `/api/cards/:id`       | GET         | Fetch details of a specific card.        | Yes                      | Regular User/Admin    |
| `/api/cards`           | POST        | Submit a new Pokémon card.               | Yes                      | Regular User          |
| `/api/cards/:id`       | PUT         | Update a Pokémon card's details.         | Yes                      | Admin                 |
| `/api/cards/:id`       | DELETE      | Delete a Pokémon card.                   | Yes                      | Admin                 |
| `/api/decks`           | GET         | Fetch all decks created by the user.     | Yes                      | Regular User/Admin    |
| `/api/decks/:id`       | GET         | Fetch details of a specific deck.        | Yes                      | Regular User/Admin    |
| `/api/decks`           | POST        | Create a new deck.                       | Yes                      | Regular User          |
| `/api/decks/:id`       | PUT         | Update details of an existing deck.      | Yes                      | Regular User          |
| `/api/decks/:id`       | DELETE      | Delete a deck.                           | Yes                      | Regular User/Admin    |
| `/api/admin/approve`   | POST        | Approve a submitted Pokémon card.        | Yes                      | Admin                 |
| `/api/admin/reject`    | POST        | Reject a submitted Pokémon card.         | Yes                      | Admin                 |
| `/api/admin/users`     | GET         | Fetch all user details.                  | Yes                      | Admin                 |
| `/api/admin/users/:id` | DELETE      | Delete a user.                           | Yes                      | Admin                 |
| `/api/admin/cards`     | GET         | Fetch all submitted cards for approval.  | Yes                      | Admin                 |
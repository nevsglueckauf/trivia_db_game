# Design & Architecture Dossier

## Sequence diagram 

```mermaid
sequenceDiagram
    autonumber
    App->>API: https://opentdb.com/api.php?amount={:AMOUNT}
    API-->>App: List of questions (JSON)
    App->>Python:  Parse JSON, generate entity instances 
    Python->>App:  Rendering questions
    User-->>App: Input (for answers) + <SUBMIT>
```


# Applicazione AI basata su MCP

Questa directory contiene un esempio di implementazione minimalista di un chatbot
che utilizza il **Model Context Protocol (MCP)** per orchestrare diversi tool.
L'utente può impartire istruzioni in linguaggio naturale indicando il tool da
utilizzare. I tool inclusi sono:

- **Google Sheets**: lettura/scrittura (placeholder).
- **Gmail**: invio di email (placeholder).
- **Instantly.ai**: attivazione di campagne di outreach (placeholder).

L'obiettivo è mostrare come mantenere una struttura modulare e trasparente,
così da poter aggiungere in futuro altri canali o servizi.

## Avvio veloce

```bash
python -m mcp_app.main
```

Digitare un'istruzione prefissata dal nome del tool, ad esempio:

```
 gmail invia a foo@example.com
 sheets leggi tabella1
 instantly avvia campagna X
```

Il codice restituisce un messaggio di conferma senza eseguire realmente le
operazioni. Per l'integrazione reale occorre completare la logica nei file di
`mcp_app/tools`.

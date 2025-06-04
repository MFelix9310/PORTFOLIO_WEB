# React Integration
REACT_ENABLED = True

# Include this in context processors
TEMPLATES = [
    {
        # ...existing template configuration...
        'OPTIONS': {
            'context_processors': [
                # ... existing context processors...
                'portfolio.context_processors.react_enabled',
            ],
        },
    },
] 
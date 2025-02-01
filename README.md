# Deploying app on streamlit cloud

## Prepare app

Write your own streamlit app.

Here is a good tutorial.

https://docs.streamlit.io/get-started

In this repository `app.py` is my streamlit application.

## Organize project and push to Github

Documentation: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/file-organization

In the simplest case, following files are sufficient.

```
repository_root/
├── requirements.txt
└── app.py
```

## Deploy

Documentation: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

Sign-in to share.streamlit.io and deploy using Github URL.
Your app users do not require an account on streamlit.io.

That's all!

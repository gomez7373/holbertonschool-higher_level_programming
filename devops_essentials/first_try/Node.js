name: Docker Image CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          node-version: '20'
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1
        with:
          node-version: '20'
          
      # Add other steps here


# DEPLOY BACK-END

### Unzip Archive
```unzip archive shipments-master.zip ```

### Change Dir
```cd shipments-master ```

### Build Docker 
```sudo docker build -t shipments -f Dockerfile .```

### Start Docker-Compose
```sudo docker-compose up```

### Api URL List Shipments
http://0.0.0.0:8000/api/v1/shipments/



# DEPLOY FRONT-END

### Unzip Archive
```unzip archive shipments-ui.zip ```

### Change Dir
```cd shipments-ui ```

### NPM Install 
```npm install```

### Build WebUI
```npm run build```

### Start Tests
```npm run:unit```

### Start Build
```npx serve -s dist```

### WebUI Location
http://localhost:3000

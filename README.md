# DIT266 - Cloud Computing


### 1. **diagrams/diagram_DIT266.png**
- **Το διάγραμμα αρχιτεκτονικής** – δείχνει το Project, Internal/External Network (Neutron), Subnet, Router, τα VMs (web/db), Floating IP, Security Groups.
  

### 2. **cloud-init/**
- **db-init.yaml:** Script cloud-init που αυτοματοποιεί την εγκατάσταση και ρύθμιση PostgreSQL στο db-vm.
- **web-init.yaml:** Script cloud-init για εγκατάσταση Java/Maven/Node.js, clone & build της εφαρμογής, εκκίνηση backend/frontend στο web-vm.

### 3. **report/report.md**
- Το πλήρες report σου (όλη η τεκμηρίωση, τα βήματα, τα προβλήματα που αντιμετώπισες, το υποθετικό σενάριο, τελικός πίνακας κόστους, επίλογος κλπ).




![networkTopology](https://github.com/user-attachments/assets/d8cdebf5-f1ad-4a1e-b700-7ad9e2167456)



![diagramDIT266](https://github.com/user-attachments/assets/4054f5d7-eb2a-4cbf-bd4c-6bd20b2986a9)

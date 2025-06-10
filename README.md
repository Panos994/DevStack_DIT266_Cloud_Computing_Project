# DIT266

## Τι περιλαμβάνει κάθε φάκελος/αρχείο

### 1. **diagrams/architecture.png**
- **Το διάγραμμα αρχιτεκτονικής** που έφτιαξες στο draw.io – δείχνει το Project, Internal/External Network (Neutron), Subnet, Router, τα VMs (web/db), Floating IP, Security Groups, Monitoring.
- Εάν έχεις και δεύτερο διάγραμμα (π.χ. ροή δεδομένων ή monitoring), βάλε το επίσης εδώ.

### 2. **cloud-init/**
- **db-init.yaml:** Script cloud-init που αυτοματοποιεί την εγκατάσταση και ρύθμιση PostgreSQL στο db-vm.
- **web-init.yaml:** Script cloud-init για εγκατάσταση Java/Maven/Node.js, clone & build της εφαρμογής, εκκίνηση backend/frontend στο web-vm.

### 3. **logs/**
- **cloud-init-output-db.txt:** Log/output από το cloud-init του db-vm (το παίρνεις από `/var/log/cloud-init-output.log` του instance).
- **cloud-init-output-web.txt:** Log/output από το cloud-init του web-vm.
- **screenshots/** (υποφάκελος):
    - **horizon-network.png:** Screenshot από το Horizon όπου φαίνεται το δίκτυο/subnet/router.
    - **monitoring-top.png:** Screenshot από εντολή `top` ή monitoring εργαλείο.
    - **app-running.png:** Απόδειξη ότι η εφαρμογή τρέχει (π.χ. browser ή curl).

### 4. **report/report.md**
- Το πλήρες report σου (όλη η τεκμηρίωση, τα βήματα, τα προβλήματα που αντιμετώπισες, το υποθετικό σενάριο, τελικός πίνακας κόστους, επίλογος κλπ).

### 5. **README.md**
- **Σύντομες οδηγίες για το repo**:  
  - Τι περιέχει το κάθε φάκελος/αρχείο.
  - Πώς να αναπαράγει κάποιος το project (π.χ. βήματα deployment).
  - Πού να βρει τα scripts, τα logs, τα screenshots, το διάγραμμα.

---

## Παράδειγμα περιεχομένου cloud-init (db-init.yaml)

```yaml
#cloud-config
package_update: true
package_upgrade: true
packages:
  - postgresql
  - postgresql-contrib
runcmd:
  - sudo -u postgres psql -c "CREATE DATABASE order_system_db;"
  - sudo -u postgres psql -c "CREATE USER dbuser WITH ENCRYPTED PASSWORD 'pass123';"
  - sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE order_system_db TO dbuser;"
  - sudo sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" /etc/postgresql/*/main/postgresql.conf
  - echo "host all all 10.0.0.0/24 md5" | sudo tee -a /etc/postgresql/*/main/pg_hba.conf
  - sudo systemctl restart postgresql
  - sudo ufw allow 5432/tcp
  - sudo ufw --force enable
```

$appSecret="P-C8Q~Rx1pRGbaeMVqrGMK-yi6CRA8ReMYayPdlK"

$appId="e9c08c32-094d-4473-aaa2-3bd002e8e8b8"

$tenantId="3bf3cf81-25c1-49e5-8989-85ec9cfda95a"

$subcriptionId="85b1fabc-aa3d-442d-bdf8-62623befad55"

$subcriptionName="Azure Pass - Sponsorship"

$resourceGroup="rgBricks1"

# Login to Azure using the Service Principal
#az login (open the browser asking you to login to your Tenant using user principal)

az login --service-principal --username $appId --password $appSecret --tenant $tenantId

#set the subscription 
az account set --name --subscription $subscriptionName


#attach to resource group
az group create --name $resourceGroup --location "East US"

#create the databricks workspace
az databricks workspace create --resource-group $resourceGroup --name carao2023DatabricksWorkspace --location "East US" --sku standard

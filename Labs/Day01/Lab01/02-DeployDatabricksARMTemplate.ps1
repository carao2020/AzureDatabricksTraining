$appSecret="P-C8Q~Rx1pRGbaeMVqrGMK-yi6CRA8ReMYayPdlK"

$appId="e9c08c32-094d-4473-aaa2-3bd002e8e8b8"

$tenantId="3bf3cf81-25c1-49e5-8989-85ec9cfda95a"

$subcriptionId="85b1fabc-aa3d-442d-bdf8-62623befad55"

$subcriptionName="Azure Pass - Sponsorship"

$resourceGroup="rgBricks"

# Login to Azure using the Service Principal
#az login (open the browser asking you to login to your Tenant using user principal)

az login --service-principal --username $appId --password $appSecret --tenant $tenantId

#set the subscription 
az account set --subscription --name $subscriptionName


#deploy using ARM templates
az deployment group create --resource-group  $resourceGroup --template-file azuredeploy.json --parameters azuredeploy.parameters.json

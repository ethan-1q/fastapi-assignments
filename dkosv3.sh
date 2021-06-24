DKOSV3_PATH=./dkosv3

kubectl delete -f $DKOSV3_PATH/deployment.yaml
kubectl delete -f $DKOSV3_PATH/service.yaml
kubectl delete -f $DKOSV3_PATH/ingress.yaml
kubectl apply -f $DKOSV3_PATH/deployment.yaml
kubectl apply -f $DKOSV3_PATH/service.yaml
kubectl apply -f $DKOSV3_PATH/ingress.yaml

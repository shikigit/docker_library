# -*- coding: utf-8 -*-

from fabric.api import *

image_str  = """kube-proxy-amd64:v1.5.2
kube-discovery-amd64:1.0
kubedns-amd64:1.10.1
kube-scheduler-amd64:v1.5.2
kube-controller-manager-amd64:v1.5.2
kube-apiserver-amd64:v1.5.2
etcd-amd64:3.0.14-kubeadm
kube-dnsmasq-amd64:1.10.1
exechealthz-amd64:1.2
pause-amd64:3.0
kubernetes-dashboard-amd64:v1.4.0"""

for image in image_str.strip().split():
    image_name = image.strip().split(':')[0]
    image_version = image.strip().split(':')[1]
    local("mkdir %s" % image_name)
    fd = open("%s/Dockerfile" % image_name, 'w')
    fd.write("FROM gcr.io/google_containers/%s\n" % image.strip())
    fd.write("MAINTAINER <shikigit>\n")
    fd.close()


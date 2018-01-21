#!/usr/bin/env python

import graphene


class RackUnit(graphene.Interface):
    positions = graphene.Int()


class Server(graphene.ObjectType):
    """
    Server
    """
    class Meta:
        interfaces = (RackUnit,)

    hostname = graphene.String()


class Plug(graphene.ObjectType):
    name = graphene.String()


class PDU(graphene.ObjectType):
    plugs = graphene.List(Plug)


class Rack(graphene.ObjectType):
    servers = graphene.List(Server)

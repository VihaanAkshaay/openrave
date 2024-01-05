import copy

_ = lambda x: x

poseSchema = {
    "title": _("Cartesian pose"),
    "description": _(
        "A 7-element vector representing a 6D cartesian pose. Consists of a wxyz quaternion and an xyz position. The quaternion defines the orientation."
    ),
    "type": "array",
    "items": [
        {"title": _("w (quaternion)"), "type": "number", "default": 1.0},
        {"title": _("x (quaternion)"), "type": "number", "default": 0.0},
        {"title": _("y (quaternion)"), "type": "number", "default": 0.0},
        {"title": _("z (quaternion)"), "type": "number", "default": 0.0},
        {"title": _("x (position)"), "type": "number", "default": 0.0, "semanticType": "Length"},
        {"title": _("y (position)"), "type": "number", "default": 0.0, "semanticType": "Length"},
        {"title": _("z (position)"), "type": "number", "default": 0.0, "semanticType": "Length"},
    ],
    "minItems": 7,
    "maxItems": 7,
    "additionalItems": False,
    "semanticType": "Pose",
    "typeName": "Transform",
    "scaleInSerialization": True
}

def MakePoseSchema(title, description):
    customPoseSchema = copy.deepcopy(poseSchema)
    customPoseSchema["title"] = title
    customPoseSchema["description"] = description
    customPoseSchema["default"] = "Transform{}"
    return customPoseSchema

geometryInfoSchema = {  # TODO(felixvd): Link to kinbody.GeometryInfo
    "type": "object",
    "typeName": "GeometryInfo",
    "properties": {
        "id": {
            "type": "string",
            "default": "",
        },
        "name": {"type": "string"},
        "type": {
            "type": "string",
            "typeName": "GeometryType",
            "enum": [
                ("none", "GT_None"),
                ("box", "GT_Box"),
                ("sphere", "GT_Sphere"),
                ("cylinder", "GT_Cylinder"),
                ("trimesh", "GT_TriMesh"),
                ("container", "GT_Container"),
                ("cage", "GT_Cage"),
                ("calibrationboard", "GT_CalibrationBoard"),
                ("axial", "GT_Axial"),
                ("conicalfrustum", "GT_ConicalFrustum"),
            ]
        },
        "diffuseColor": {
            'type': 'array',
            'minItems': 3,
            'maxItems': 3,
            'items': {
                'type': 'number'
            },
            "typeName": "RaveVector<float>",
            "default": "RaveVector<float>{1, 1, 1}",
        },
        "ambientColor": {
            'type': 'array',
            'minItems': 3,
            'maxItems': 3,
            'items': {
                'type': 'number'
            },
            "typeName": "RaveVector<float>",
            "default": "RaveVector<float>{}",
        },
        "outerExtents": {
            "type": "array",
            "minItems": 3,
            "maxItems": 3,
            "items": {
                "type": "number"
            },
            "typeName": "Vector",
            "scaleInSerialization": True
        },
        "innerExtents": {
            "type": "array",
            "minItems": 3,
            "maxItems": 3,
            "items": {
                "type": "number"
            },
            "typeName": "Vector",
            "scaleInSerialization": True

        },
        "halfExtents": {
            "type": "array",
            "minItems": 3,
            "maxItems": 3,
            "items": {
                "type": "number"
            },
            "typeName": "Vector",
            "scaleInSerialization": True

        },
        "transparency": {
            "type": "number"
        },
        "negativeCropContainerMargins": {
            "type": "array",
            "minItems": 3,
            "maxItems": 3,
            "items": {
                "type": "number"
            },
            "typeName": "Vector",
            "default": "Vector(0, 0, 0)",
            "scaleInSerialization": True

        },
        "negativeCropContainerEmptyMargins": {
            "type": "array",
            "minItems": 3,
            "maxItems": 3,
            "items": {
                "type": "number"
            },
            "typeName": "Vector",
            "default": "Vector(0, 0, 0)",
            "scaleInSerialization": True

        },
        "positiveCropContainerMargins": {
            "type": "array",
            "minItems": 3,
            "maxItems": 3,
            "items": {
                "type": "number"
            },
            "typeName": "Vector",
            "default": "Vector(0, 0, 0)",
            "scaleInSerialization": True

        },
        "positiveCropContainerEmptyMargins": {
            "type": "array",
            "minItems": 3,
            "maxItems": 3,
            "items": {
                "type": "number"
            },
            "typeName": "Vector",
            "default": "Vector(0, 0, 0)",
            "scaleInSerialization": True

        },
        "transform": MakePoseSchema(title=_("transform"), description=_("transform")),
        "visible": {
            "type": "boolean",
            "default": True
        },
        "transparency": {
            "type": "number",
            "typeName": "float",
            "default": 0
        }
    },
    "required": ["id", "name"]
}

geometryInfosSchema = {
    "type": "array",
    "description": _("list of serialized geometry infos of the base link when the first geometry is cage (for now)"),
    "items": geometryInfoSchema,
}
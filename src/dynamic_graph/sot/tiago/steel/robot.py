# -*- coding: utf-8 -*-
# Copyright 2016, Olivier Stasse, CNRS

from dynamic_graph.sot.tiago import Tiago


class TiagoSteel(Tiago):
    """
    This class instantiates LAAS TIAGO Robot
    """
    def __init__(self, name, device=None, tracer=None, with_wheels=True):
        halfSitting = (
            0.,
            0.,
            0.,
            0.,
            0.,
            0.,
        ) + ((
            0.,
            0.,
        ) if with_wheels else tuple()  # Wheels
             ) + (
                 0.,  # Torso
                 0.,
                 -1.569796,
                 -1.569796,
                 2.355194,
                 0.,
                 0.,
                 0.,  # Arm
                 0.,  # Gripper (left, right)
                 0.,
                 0.,  # Head
             )
        Tiago.__init__(self, name, initialConfig=halfSitting, device=device, tracer=tracer, with_wheels=with_wheels)
        """
        TODO:Confirm these values
        # Define camera positions w.r.t gaze.
        cameraBottomLeftPosition = np.matrix((
            (0.98481, 0.00000, 0.17365, 0.035),
            (0.,      1.,      0.,      0.072),
            (-0.17365, 0.00000, 0.98481, 0.075 - 0.03),
            (0., 0., 0., 1.),
        ))
        cameraBottomRightPosition = np.matrix((
            (0.98481, 0.00000, 0.17365, 0.035),
                (0.,      1.,      0.,     -0.072),
                (-0.17365, 0.00000, 0.98481, 0.075 - 0.03),
                (0., 0., 0., 1.),
                ))
        cameraTopLeftPosition = np.matrix((
            (0.99920,  0.00120, 0.03997, 0.01),
            (0.00000,  0.99955,-0.03000, 0.029),
            (-0.03999, 0.02997, 0.99875, 0.145 - 0.03),
            (0.,       0.,      0.,      1.),
        ))
        cameraTopRightPosition = np.matrix((
            (0.99920,  0.00000, 0.03999,  0.01),
            (0.00000,  1.00000, 0.00000, -0.029),
            (-0.03999, 0.00000, 0.99920,  0.145 - 0.03),
            (0.,       0.,      0.,       1.),
        ))
        # Frames re-orientation:
        # Z = depth (increase from near to far)
        # X = increase from left to right
        # Y = increase from top to bottom

        c1_M_c = np.matrix(
            [[ 0.,  0.,  1., 0.],
             [-1.,  0.,  0., 0.],
             [ 0., -1.,  0., 0.],
             [ 0.,  0.,  0., 1.]])

        for camera in [cameraBottomLeftPosition, cameraBottomRightPosition,
                       cameraTopLeftPosition, cameraTopRightPosition]:
            camera[:] = camera * c1_M_c

        self.AdditionalFrames.append(
            ("cameraBottomLeft",
             matrixToTuple(cameraBottomLeftPosition), "gaze"))
        self.AdditionalFrames.append(
            ("cameraBottomRight",
             matrixToTuple(cameraBottomRightPosition), "gaze"))
        self.AdditionalFrames.append(
            ("cameraTopLeft",
             matrixToTuple(cameraTopLeftPosition), "gaze"))
        self.AdditionalFrames.append(
            ("cameraTopRight",
             matrixToTuple(cameraTopRightPosition), "gaze"))
        """


__all__ = ["TiagoSteel"]

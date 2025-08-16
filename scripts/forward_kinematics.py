import numpy as np

def dh_transform(a, alpha, d, theta):
    """
    Create the Denavit-Hartenberg transformation matrix.
    a: link length
    alpha: link twist
    d: link offset
    theta: joint angle
    """
    sa, ca = np.sin(alpha), np.cos(alpha)
    st, ct = np.sin(theta), np.cos(theta)
    
    return np.array([
        [ct, -st * ca,  st * sa, a * ct],
        [st,  ct * ca, -ct * sa, a * st],
        [0,      sa,       ca,      d ],
        [0,       0,        0,      1 ]
    ])

def forward_kinematics(joints, L=1.0):
    """
    Calculate end-effector position for 4-DOF robot arm.
    joints: list or tuple of 4 joint angles (radians): [j1, j2, j3, j4]
    L: length of each link
    
    Returns:
        x, y, z coordinates of the end-effector
    """
    j1, j2, j3, j4 = joints
    
    # DH Parameters for each link [a, alpha, d, theta]
    # Here, axis twist alpha alternates ±90deg (±pi/2) due to perpendicular axes
    dh_params = [
        [L,  np.pi/2, 0,      j1],
        [L, -np.pi/2, 0,      j2],
        [L,  np.pi/2, 0,      j3],
        [L,        0, 0,      j4]
    ]
    
    # Start with identity matrix
    T = np.eye(4)

    # Multiply the transforms for each link
    for a, alpha, d, theta in dh_params:
        T = np.dot(T, dh_transform(a, alpha, d, theta))

    # Extract position of end effector
    x, y, z = T[0, 3], T[1, 3], T[2, 3]
    return x, y, z

if __name__ == "__main__":
    # Example use:
    # Define joint angles in radians
    joints = [np.deg2rad(30), np.deg2rad(45), np.deg2rad(-30), np.deg2rad(60)]

    x, y, z = forward_kinematics(joints)
    print(f"End-effector position: x={x:.3f}, y={y:.3f}, z={z:.3f}")

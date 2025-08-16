import math

def euler_to_quaternion(roll, pitch, yaw):
    """
    Convert Euler angles (roll, pitch, yaw) to quaternion (x, y, z, w).
    All angles are in radians.
    Rotation order is ZYX (yaw-pitch-roll).
    
    Returns:
        (x, y, z, w) quaternion
    """
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)

    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy

    return x, y, z, w


def quaternion_to_euler(x, y, z, w):
    """
    Convert quaternion (x, y, z, w) to Euler angles (roll, pitch, yaw).
    Returns angles in radians.
    Rotation order is ZYX (yaw-pitch-roll).

    Handles edge cases like gimbal lock gracefully.

    Returns:
        roll, pitch, yaw (in radians)
    """
    # Roll (x-axis rotation)
    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x * x + y * y)
    roll = math.atan2(sinr_cosp, cosr_cosp)

    # Pitch (y-axis rotation)
    sinp = 2 * (w * y - z * x)
    if abs(sinp) >= 1:
        # Use 90 degrees if out of range (gimbal lock)
        pitch = math.copysign(math.pi / 2, sinp)
    else:
        pitch = math.asin(sinp)

    # Yaw (z-axis rotation)
    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y * y + z * z)
    yaw = math.atan2(siny_cosp, cosy_cosp)

    return roll, pitch, yaw


if __name__ == "__main__":
    # Example usage:
    import numpy as np

    # Define Euler angles (radians)
    roll = np.deg2rad(45)
    pitch = np.deg2rad(30)
    yaw = np.deg2rad(60)

    print(f"Original Euler angles (deg): Roll={np.rad2deg(roll):.2f}, Pitch={np.rad2deg(pitch):.2f}, Yaw={np.rad2deg(yaw):.2f}")

    # Convert to quaternion
    qx, qy, qz, qw = euler_to_quaternion(roll, pitch, yaw)
    print(f"Quaternion: x={qx:.4f}, y={qy:.4f}, z={qz:.4f}, w={qw:.4f}")

    # Convert back to Euler angles
    r, p, y = quaternion_to_euler(qx, qy, qz, qw)
    print(f"Converted Euler angles (deg): Roll={np.rad2deg(r):.2f}, Pitch={np.rad2deg(p):.2f}, Yaw={np.rad2deg(y):.2f}")

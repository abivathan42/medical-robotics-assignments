import time, math
import browserbotics as bb

bb.setGravity(0, 0, -9.8)
bb.addGroundPlane()
time.sleep(1.0)

# ── FLOOR ──────────────────────────────────────────────────
bb.createBody('box', halfExtent=[4.0, 5.0, 0.02],
    position=[0.0, 0.0, -0.02], color=0xD4C5B0, mass=0)
time.sleep(1.0)

# ── BACK WALL ──────────────────────────────────────────────
bb.createBody('box', halfExtent=[4.0, 0.05, 2.0],
    position=[0.0, 5.0, 2.0], color=0xA8DFC0, mass=0)
time.sleep(1.0)

# ── LEFT WALL ──────────────────────────────────────────────
bb.createBody('box', halfExtent=[0.05, 5.0, 2.0],
    position=[-4.0, 0.0, 2.0], color=0xB8DCF5, mass=0)
time.sleep(1.0)

# ── RIGHT WALL ─────────────────────────────────────────────
bb.createBody('box', halfExtent=[0.05, 5.0, 2.0],
    position=[4.0, 0.0, 2.0], color=0xB8DCF5, mass=0)
time.sleep(1.0)

# ── FRONT WALL LEFT SECTION (beside door) ──────────────────
bb.createBody('box', halfExtent=[1.5, 0.05, 2.0],
    position=[-2.5, -5.0, 2.0], color=0xB8DCF5, mass=0)
time.sleep(1.0)

# ── FRONT WALL RIGHT SECTION (beside door) ─────────────────
bb.createBody('box', halfExtent=[1.5, 0.05, 2.0],
    position=[2.5, -5.0, 2.0], color=0xB8DCF5, mass=0)
time.sleep(1.0)

# ── FRONT WALL ABOVE DOOR ──────────────────────────────────
bb.createBody('box', halfExtent=[1.0, 0.05, 0.55],
    position=[0.0, -5.0, 3.45], color=0xB8DCF5, mass=0)
time.sleep(1.0)

# ── DOOR FRAME LEFT ────────────────────────────────────────
bb.createBody('box', halfExtent=[0.06, 0.08, 1.50],
    position=[-1.0, -4.97, 1.50], color=0xC8A870, mass=0)
time.sleep(1.0)

# ── DOOR FRAME RIGHT ───────────────────────────────────────
bb.createBody('box', halfExtent=[0.06, 0.08, 1.50],
    position=[1.0, -4.97, 1.50], color=0xC8A870, mass=0)
time.sleep(1.0)

# ── DOOR FRAME TOP ─────────────────────────────────────────
bb.createBody('box', halfExtent=[1.06, 0.08, 0.06],
    position=[0.0, -4.97, 3.0], color=0xC8A870, mass=0)
time.sleep(1.0)

# ── DOOR PANEL LEFT HALF ───────────────────────────────────
door_left = bb.createBody('box', halfExtent=[0.48, 0.04, 1.44],
    position=[-0.50, -4.95, 1.50], color=0xDEB887, mass=0)
time.sleep(1.0)

# ── DOOR PANEL RIGHT HALF ──────────────────────────────────
door_right = bb.createBody('box', halfExtent=[0.48, 0.04, 1.44],
    position=[0.50, -4.95, 1.50], color=0xDEB887, mass=0)
time.sleep(1.0)

# ── DOOR HANDLES ───────────────────────────────────────────
bb.createBody('box', halfExtent=[0.04, 0.06, 0.04],
    position=[-0.08, -4.90, 1.50], color=0xAAAA00, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.04, 0.06, 0.04],
    position=[0.08, -4.90, 1.50], color=0xAAAA00, mass=0)
time.sleep(1.0)

# ── CEILING ────────────────────────────────────────────────
bb.createBody('box', halfExtent=[4.0, 5.0, 0.02],
    position=[0.0, 0.0, 4.02], color=0xFFFFFF, mass=0)
time.sleep(1.0)

# ── CEILING LIGHT ──────────────────────────────────────────
bb.createBody('box', halfExtent=[1.5, 0.10, 0.02],
    position=[0.0, 0.0, 3.98], color=0xFFFBCC, mass=0)
time.sleep(1.0)

# ── WINDOW ─────────────────────────────────────────────────
bb.createBody('box', halfExtent=[0.60, 0.05, 0.50],
    position=[2.0, 4.94, 2.2], color=0xF0F0F0, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.55, 0.03, 0.45],
    position=[2.0, 4.94, 2.2], color=0x77BBFF, mass=0)
time.sleep(1.0)
print("room ok")

# ── WALL EQUIPMENT PANEL ───────────────────────────────────
bb.createBody('box', halfExtent=[0.05, 0.50, 0.40],
    position=[-3.94, 1.5, 1.6], color=0x2244AA, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.03, 0.05, 0.05],
    position=[-3.94, 1.6, 1.80], color=0x11CC44, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.03, 0.05, 0.05],
    position=[-3.94, 1.5, 1.60], color=0xFFCC00, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.03, 0.05, 0.05],
    position=[-3.94, 1.4, 1.40], color=0xDD3300, mass=0)
time.sleep(1.0)

# ── CO2 PIPELINE ───────────────────────────────────────────
bb.createBody('box', halfExtent=[0.03, 2.5, 0.03],
    position=[-3.94, 1.0, 2.3], color=0x2244AA, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.03, 0.03, 0.6],
    position=[-3.94, 1.5, 1.9], color=0x2244AA, mass=0)
time.sleep(1.0)

# ── CO2 CYLINDER ───────────────────────────────────────────
bb.createBody('box', halfExtent=[0.15, 0.15, 0.60],
    position=[-3.5, 4.5, 0.60], color=0x006400, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.10, 0.10, 0.12],
    position=[-3.5, 4.5, 1.32], color=0x111111, mass=0)
time.sleep(1.0)
print("equipment ok")

# ── IV DRIP STAND ──────────────────────────────────────────
bb.createBody('box', halfExtent=[0.015, 0.015, 0.95],
    position=[-0.85, -0.5, 0.95], color=0xCCCDD0, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.06, 0.02, 0.11],
    position=[-0.76, -0.5, 1.97], color=0x44DDF0, mass=0)
time.sleep(1.0)

# ── VITAL SIGNS MONITOR ────────────────────────────────────
bb.createBody('box', halfExtent=[0.02, 0.02, 0.60],
    position=[-0.85, 1.5, 0.60], color=0x333340, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.24, 0.06, 0.18],
    position=[-0.85, 1.5, 1.30], color=0x1A1A28, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.22, 0.01, 0.16],
    position=[-0.85, 1.44, 1.30], color=0x00F060, mass=0)
time.sleep(1.0)

# ── OVERHEAD SURGICAL LIGHT ────────────────────────────────
bb.createBody('box', halfExtent=[0.02, 0.02, 0.45],
    position=[0.0, 0.0, 3.55], color=0x888888, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.32, 0.32, 0.06],
    position=[0.0, 0.0, 3.10], color=0xFFF5AA, mass=0)
time.sleep(1.0)
print("monitors ok")

# ── SURGEON CONSOLE ────────────────────────────────────────
bb.createBody('box', halfExtent=[0.50, 0.35, 0.55],
    position=[-2.8, 4.0, 0.55], color=0x1A1A2E, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.38, 0.03, 0.28],
    position=[-2.8, 3.67, 1.45], color=0x0044CC, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.36, 0.01, 0.26],
    position=[-2.8, 3.66, 1.45], color=0x00CCFF, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.08, 0.06, 0.06],
    position=[-2.95, 3.70, 1.20], color=0x111111, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.08, 0.06, 0.06],
    position=[-2.65, 3.70, 1.20], color=0x111111, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.06, 0.06, 0.12],
    position=[-3.1, 3.85, 1.10], color=0x333344, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.06, 0.06, 0.12],
    position=[-2.5, 3.85, 1.10], color=0x333344, mass=0)
time.sleep(1.0)
print("console ok")

# ── SURGERY TOWER ──────────────────────────────────────────
bb.createBody('box', halfExtent=[0.20, 0.20, 0.90],
    position=[-1.5, -0.5, 0.90], color=0x2A2A3E, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.15, 0.03, 0.10],
    position=[-1.5, -0.70, 1.60], color=0x00AA44, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.03, 0.02, 0.03],
    position=[-1.50, -0.70, 1.75], color=0x00FF44, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.03, 0.02, 0.03],
    position=[-1.58, -0.70, 1.75], color=0xFFAA00, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.03, 0.02, 0.03],
    position=[-1.42, -0.70, 1.75], color=0xFF2200, mass=0)
time.sleep(1.0)

# ── OVERHEAD SURGERY BOOM ──────────────────────────────────
bb.createBody('box', halfExtent=[0.06, 0.06, 0.08],
    position=[0.0, -0.3, 3.95], color=0x555566, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[1.6, 0.05, 0.05],
    position=[0.0, -0.3, 3.87], color=0x666677, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.03, 0.03, 0.40],
    position=[-1.5, -0.3, 3.67], color=0x666677, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.03, 0.03, 0.40],
    position=[1.5, -0.3, 3.67], color=0x666677, mass=0)
time.sleep(1.0)
print("surgery setup ok")

# ── SURGERY TOOL TIPS (animated) ───────────────────────────
scalpel_tip = bb.createBody('box', halfExtent=[0.008, 0.008, 0.06],
    position=[-1.1, -0.1, 1.58], color=0xDDDDEE, mass=0)
time.sleep(1.0)
camera_tip = bb.createBody('box', halfExtent=[0.04, 0.04, 0.05],
    position=[1.1, -0.5, 1.36], color=0x111122, mass=0)
time.sleep(1.0)
cauterizer_tip = bb.createBody('box', halfExtent=[0.015, 0.015, 0.05],
    position=[0.0, -0.9, 1.56], color=0xFF6600, mass=0)
time.sleep(1.0)

# ── MEDICAL TROLLEY ────────────────────────────────────────
TR_X, TR_Y = 2.5, -1.5
bb.createBody('box', halfExtent=[0.30, 0.22, 0.38],
    position=[TR_X, TR_Y, 0.38], color=0x7AAEDD, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.30, 0.22, 0.02],
    position=[TR_X, TR_Y, 0.78], color=0xF7F7FC, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.028, 0.028, 0.058],
    position=[TR_X-0.10, TR_Y-0.10, 0.84], color=0xCC6600, mass=0)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.028, 0.028, 0.014],
    position=[TR_X-0.10, TR_Y-0.10, 0.912], color=0xCC1010, mass=0)
time.sleep(1.0)
medicine_box = bb.createBody('box', halfExtent=[0.08, 0.06, 0.05],
    position=[TR_X-0.10, TR_Y-0.10, 0.92], color=0xCC6600, mass=0)
time.sleep(1.0)
print("trolley ok")

# ── VACUUM ROBOT ───────────────────────────────────────────
vac_body = bb.createBody('box', halfExtent=[0.22, 0.22, 0.07],
    position=[-3.0, -4.0, 0.07], color=0x222222, mass=1)
time.sleep(1.0)
bb.createBody('box', halfExtent=[0.15, 0.15, 0.05],
    position=[-3.0, -4.0, 0.16], color=0x555555, mass=0)
time.sleep(1.0)
print("vacuum ok")

# ── BED + PATIENT ──────────────────────────────────────────
# bed_height now goes both UP and DOWN correctly
bb.addDebugSlider('bed_height', 0.38, 0.20, 0.90)

def build_bed_and_patient(bz):
    for lx, ly in [(-0.45,-1.0),(0.45,-1.0),(-0.45,1.0),(0.45,1.0)]:
        bb.createBody('box', halfExtent=[0.04, 0.04, bz/2],
            position=[lx, ly, bz/2], color=0x9AA0A8, mass=0)
        time.sleep(0.2)
    bb.createBody('box', halfExtent=[0.50, 1.05, 0.04],
        position=[0.0, 0.0, bz], color=0xB8BBBF, mass=0)
    time.sleep(0.2)
    bb.createBody('box', halfExtent=[0.47, 1.02, 0.09],
        position=[0.0, 0.0, bz+0.11], color=0xF5F5F5, mass=0)
    time.sleep(0.2)
    bb.createBody('box', halfExtent=[0.46, 1.01, 0.02],
        position=[0.0, 0.0, bz+0.21], color=0x5599E8, mass=0)
    time.sleep(0.2)
    bb.createBody('box', halfExtent=[0.50, 0.04, 0.35],
        position=[0.0, 1.08, bz+0.38], color=0x1F6B7A, mass=0)
    time.sleep(0.2)
    bb.createBody('box', halfExtent=[0.50, 0.04, 0.20],
        position=[0.0, -1.08, bz+0.22], color=0x1F6B7A, mass=0)
    time.sleep(0.2)
    pz = bz + 0.24
    bb.createBody('box', halfExtent=[0.19, 0.32, 0.08],
        position=[0.0, 0.15, pz+0.02], color=0xF5C5A0, mass=0)
    time.sleep(0.2)
    bb.createBody('box', halfExtent=[0.20, 0.33, 0.02],
        position=[0.0, 0.15, pz+0.11], color=0x88BBEE, mass=0)
    time.sleep(0.2)
    bb.createBody('box', halfExtent=[0.05, 0.22, 0.04],
        position=[0.28, -0.05, pz], color=0xF5C5A0, mass=0)
    time.sleep(0.2)
    bb.createBody('box', halfExtent=[0.12, 0.11, 0.11],
        position=[0.0, 0.68, pz+0.11], color=0xF5C5A0, mass=0)
    time.sleep(0.2)
    bb.createBody('box', halfExtent=[0.12, 0.11, 0.03],
        position=[0.0, 0.68, pz+0.22], color=0x3B2010, mass=0)
    time.sleep(0.2)

current_bed_z = 0.38
last_bed_z    = current_bed_z
build_bed_and_patient(current_bed_z)
time.sleep(1.0)
print("bed ok")

# ── PANDA ARM ──────────────────────────────────────────────
arm_robot = bb.loadURDF('panda.urdf', position=[1.2, 0.0, 0.0], fixedBase=True)
time.sleep(2.0)
ee_link = 10
home_joints = [0, -0.5, 0.0, -1.5, 0.1, 1.0, 0]
for i, jp in enumerate(home_joints):
    bb.resetJointState(arm_robot, i, jp)
time.sleep(1.0)
print("arm ok")

# ── SPOT DOG ───────────────────────────────────────────────
spot = bb.loadURDF('spot.urdf', position=[3.0, -4.0, 0.75], fixedBase=False)
time.sleep(2.0)
print("spot ok")

front_left_hip_joint_id   = 1
front_left_knee_joint_id  = 2
front_right_hip_joint_id  = 4
front_right_knee_joint_id = 5
rear_left_hip_joint_id    = 7
rear_left_knee_joint_id   = 8
rear_right_hip_joint_id   = 10
rear_right_knee_joint_id  = 11

tau                    = 8
hip_pos_base           = 1.0
knee_pos_base          = -1.8
hip_swing_magn         = 0.5
knee_swing_magn        = 0.8
front_back_phase_delay = math.pi / 2

spot_waypoints = [
    [3.0,  -4.0, 0.75],
    [TR_X, TR_Y, 0.75],
    [0.5,  -0.5, 0.75],
    [0.5,   0.5, 0.75],
    [0.5,  -0.5, 0.75],
    [3.0,  -4.0, 0.75],
]
spot_pos      = [3.0, -4.0, 0.75]
spot_wp_index = 0
spot_speed    = 0.025
DOG_IDLE      = 0
DOG_CARRYING  = 2
DOG_DELIVERED = 3
dog_state     = DOG_IDLE

vac_waypoints = [
    [-3.0, -4.0, 0.07],
    [ 3.0, -4.0, 0.07],
    [ 3.0,  0.0, 0.07],
    [-3.0,  0.0, 0.07],
    [-3.0,  4.0, 0.07],
    [ 3.0,  4.0, 0.07],
    [ 3.0,  0.0, 0.07],
    [-3.0, -4.0, 0.07],
]
vac_pos   = [-3.0, -4.0, 0.07]
vac_index = 0
vac_speed = 0.06

# ── ARM WAYPOINTS ──────────────────────────────────────────
def get_arm_waypoints(bz):
    phz = bz + 0.24
    return [
        ([0.45, -0.3,  0.85],        [math.pi, 0, 0], 50),   # 0 home
        ([0.80, -1.0,  0.95],        [math.pi, 0, 0], 30),   # 1 approach trolley
        ([0.85, -1.4,  0.85],        [math.pi, 0, 0], 50),   # 2 reach medicine
        ([0.85, -1.4,  0.85],        [math.pi, 0, 0], 40),   # 3 grip pause
        ([0.85, -1.4,  1.10],        [math.pi, 0, 0], 40),   # 4 lift up
        ([0.40,  0.0,  1.10],        [math.pi, 0, 0], 40),   # 5 carry to patient
        ([0.30, -0.05, phz+0.08],    [math.pi, 0, 0], 80),   # 6 lower to hand
        ([0.30, -0.05, phz+0.08],    [math.pi, 0, 0], 60),   # 7 deliver pause
        ([0.30, -0.05, phz+0.40],    [math.pi, 0, 0], 30),   # 8 lift back
        ([0.45, -0.3,  0.85],        [math.pi, 0, 0], 50),   # 9 return home
    ]

arm_waypoints     = get_arm_waypoints(current_bed_z)
arm_wp_index      = 0
arm_hold_count    = 0
medicine_on_arm   = False
medicine_delivered = False

# ── SURGERY ANIMATION ──────────────────────────────────────
surgery_t = 0.0

# ── DOOR ANIMATION ─────────────────────────────────────────
door_open       = False
door_angle      = 0.0       # 0 = closed, 1 = fully open
door_open_speed = 0.03

# ── SLIDERS & TOGGLES ──────────────────────────────────────
bb.addDebugSlider('arm_x',  0.45, -1.0,  1.5)
bb.addDebugSlider('arm_y', -0.3,  -2.0,  2.0)
bb.addDebugSlider('arm_z',  0.85,  0.3,  1.8)
bb.addDebugSlider('arm_rx', math.pi, -math.pi, math.pi)
bb.addDebugSlider('arm_ry', 0.0, -math.pi, math.pi)
bb.addDebugSlider('arm_rz', 0.0, -math.pi, math.pi)
bb.addDebugToggle('use rotation')
bb.addDebugToggle('auto deliver')
bb.addDebugToggle('dog deliver')
bb.addDebugToggle('surgery mode')
bb.addDebugToggle('vacuum on')
bb.addDebugToggle('open door')

goal_frame = bb.createDebugFrame(position=[0, 0, 0], length=0.15)
frame      = bb.createDebugFrame(position=[0, 0, 0], length=0.15)

walk_i = 0
print("ALL READY — starting loop")

# ── MAIN LOOP ──────────────────────────────────────────────
while True:
    try:

        # ── BED HEIGHT (up AND down) ────────────────────────
        new_bed_z = bb.readDebugParameter('bed_height')
        # trigger rebuild whenever slider moves either direction
        if abs(new_bed_z - last_bed_z) > 0.005:
            build_bed_and_patient(new_bed_z)
            arm_waypoints = get_arm_waypoints(new_bed_z)
            last_bed_z = new_bed_z

        # ── TRACK END EFFECTOR ─────────────────────────────
        link_pose = bb.getLinkPose(arm_robot, ee_link)
        if link_pose is not None:
            bb.resetDebugObjectPose(frame, *link_pose)

        # ── PANDA ARM AUTO DELIVERY ────────────────────────
        auto = bb.readDebugParameter('auto deliver')
        if auto:
            pos, angles, hold_frames = arm_waypoints[arm_wp_index]
            quat = bb.getQuaternionFromEuler(angles)
            bb.resetDebugObjectPose(goal_frame, pos, quat)
            jpos = bb.calculateInverseKinematics(arm_robot, ee_link, pos, quat)
            if jpos:
                for i, jp in enumerate(jpos):
                    bb.setJointMotorControl(arm_robot, i, targetPosition=jp)

            # medicine follows arm from step 2 to 7
            if arm_wp_index in [2, 3, 4, 5, 6, 7]:
                medicine_on_arm    = True
                medicine_delivered = False
            elif arm_wp_index == 8:
                medicine_on_arm    = False
                medicine_delivered = True

            if medicine_on_arm and link_pose is not None:
                ep = link_pose[0]
                bb.resetDebugObjectPose(medicine_box,
                    [ep[0], ep[1], ep[2] - 0.08], [0, 0, 0, 1])
            elif medicine_delivered:
                bb.resetDebugObjectPose(medicine_box,
                    [0.28, -0.05, last_bed_z + 0.26], [0, 0, 0, 1])
            else:
                bb.resetDebugObjectPose(medicine_box,
                    [TR_X-0.10, TR_Y-0.10, 0.92], [0, 0, 0, 1])

            arm_hold_count += 1
            if arm_hold_count >= hold_frames:
                arm_hold_count = 0
                arm_wp_index   = (arm_wp_index + 1) % len(arm_waypoints)
                if arm_wp_index == 0:
                    medicine_on_arm    = False
                    medicine_delivered = False

        else:
            # manual slider control
            pos = [
                bb.readDebugParameter('arm_x'),
                bb.readDebugParameter('arm_y'),
                bb.readDebugParameter('arm_z'),
            ]
            angles = [
                bb.readDebugParameter('arm_rx'),
                bb.readDebugParameter('arm_ry'),
                bb.readDebugParameter('arm_rz'),
            ]
            use_rot = bb.readDebugParameter('use rotation')
            quat    = bb.getQuaternionFromEuler(angles)
            bb.resetDebugObjectPose(goal_frame, pos, quat)
            jpos = bb.calculateInverseKinematics(
                arm_robot, ee_link, pos, quat if use_rot else None)
            if jpos:
                for i, jp in enumerate(jpos):
                    bb.setJointMotorControl(arm_robot, i, targetPosition=jp)

        # ── SURGERY MODE ───────────────────────────────────
        surgery_on = bb.readDebugParameter('surgery mode')
        if surgery_on:
            surgery_t += 0.05
            bz = last_bed_z

            # scalpel — precise incision strokes
            sx = 0.10 * math.sin(surgery_t * 0.8)
            sy = -0.10 + 0.05 * math.sin(surgery_t * 1.2)
            sz = bz + 0.38 + 0.04 * math.cos(surgery_t * 1.5)
            bb.resetDebugObjectPose(scalpel_tip,
                [sx, sy, sz],
                bb.getQuaternionFromEuler(
                    [0, math.pi/6 * math.sin(surgery_t), 0]))

            # camera — slow sweep
            cx = 0.30 * math.cos(surgery_t * 0.3)
            cy = -0.20 + 0.15 * math.sin(surgery_t * 0.3)
            cz = bz + 0.65 + 0.05 * math.sin(surgery_t * 0.5)
            bb.resetDebugObjectPose(camera_tip,
                [cx, cy, cz],
                bb.getQuaternionFromEuler(
                    [math.pi/8, 0, surgery_t * 0.2]))

            # cauterizer — pulses
            tx = -0.12 + 0.06 * math.sin(surgery_t * 2.0)
            ty = -0.05 + 0.04 * math.cos(surgery_t * 1.8)
            tz = bz + 0.40 + 0.03 * abs(math.sin(surgery_t * 2.5))
            bb.resetDebugObjectPose(cauterizer_tip,
                [tx, ty, tz],
                bb.getQuaternionFromEuler([0, 0, surgery_t * 0.5]))
        else:
            # park tools at rest
            bb.resetDebugObjectPose(scalpel_tip,
                [-1.1, -0.1, 1.58], [0, 0, 0, 1])
            bb.resetDebugObjectPose(camera_tip,
                [1.1, -0.5, 1.36], [0, 0, 0, 1])
            bb.resetDebugObjectPose(cauterizer_tip,
                [0.0, -0.9, 1.56], [0, 0, 0, 1])

        # ── SPOT DOG ───────────────────────────────────────
        dog_on = bb.readDebugParameter('dog deliver')
        if dog_on:
            hip_f  = hip_pos_base + hip_swing_magn * math.sin(walk_i / tau)
            knee_f = knee_pos_base + knee_swing_magn * math.cos(walk_i / tau)
            for ji in [front_left_hip_joint_id, front_right_hip_joint_id]:
                bb.setJointMotorControl(spot, ji, targetPosition=hip_f)
            for ji in [front_left_knee_joint_id, front_right_knee_joint_id]:
                bb.setJointMotorControl(spot, ji, targetPosition=knee_f)
            hip_r  = hip_pos_base + hip_swing_magn * math.sin(walk_i / tau + front_back_phase_delay)
            knee_r = knee_pos_base + knee_swing_magn * math.cos(walk_i / tau + front_back_phase_delay)
            for ji in [rear_left_hip_joint_id, rear_right_hip_joint_id]:
                bb.setJointMotorControl(spot, ji, targetPosition=hip_r)
            for ji in [rear_left_knee_joint_id, rear_right_knee_joint_id]:
                bb.setJointMotorControl(spot, ji, targetPosition=knee_r)
            walk_i += 1

            target = spot_waypoints[spot_wp_index]
            dx   = target[0] - spot_pos[0]
            dy   = target[1] - spot_pos[1]
            dist = math.sqrt(dx*dx + dy*dy)
            if dist < 0.15:
                spot_wp_index = (spot_wp_index + 1) % len(spot_waypoints)
                if spot_wp_index == 2:
                    dog_state = DOG_CARRYING
                elif spot_wp_index == 4:
                    dog_state = DOG_DELIVERED
                elif spot_wp_index == 0:
                    dog_state = DOG_IDLE
            else:
                spot_pos[0] += spot_speed * dx / dist
                spot_pos[1] += spot_speed * dy / dist

            heading = math.atan2(dy, dx)
            bb.resetDebugObjectPose(spot, spot_pos,
                bb.getQuaternionFromEuler([0, 0, heading]))

        # ── VACUUM ROBOT ───────────────────────────────────
        vac_on = bb.readDebugParameter('vacuum on')
        if vac_on:
            target = vac_waypoints[vac_index]
            dx   = target[0] - vac_pos[0]
            dy   = target[1] - vac_pos[1]
            dist = math.sqrt(dx*dx + dy*dy)
            if dist < 0.10:
                vac_index = (vac_index + 1) % len(vac_waypoints)
            else:
                vac_pos[0] += vac_speed * dx / dist
                vac_pos[1] += vac_speed * dy / dist
                bb.resetDebugObjectPose(vac_body, vac_pos, [0, 0, 0, 1])

        # ── DOOR OPEN / CLOSE ──────────────────────────────
        want_open = bb.readDebugParameter('open door')
        if want_open:
            door_angle = min(1.0, door_angle + door_open_speed)
        else:
            door_angle = max(0.0, door_angle - door_open_speed)

        # left door swings left (negative x)
        left_swing  = door_angle * (-0.90)
        # right door swings right (positive x)
        right_swing = door_angle * ( 0.90)

        # pivot point is at the hinge edge of each door panel
        # left door hinge at x = -1.0, right door hinge at x = +1.0
        left_x  = -1.0 + left_swing  * math.cos(0) - 0.48
        left_y  = -4.95 + left_swing * math.sin(0)
        right_x =  1.0 + right_swing * math.cos(0) + 0.48
        right_y = -4.95

        bb.resetDebugObjectPose(door_left,
            [left_x,  left_y,  1.50],
            bb.getQuaternionFromEuler([0, 0, door_angle * math.pi / 2]))
        bb.resetDebugObjectPose(door_right,
            [right_x, right_y, 1.50],
            bb.getQuaternionFromEuler([0, 0, -door_angle * math.pi / 2]))

    except Exception as e:
        print("err:", e)

    time.sleep(0.01)

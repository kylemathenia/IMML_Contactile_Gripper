// Auto-generated. Do not edit!

// (in-package papillarray_ros_v2.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let PillarState = require('./PillarState.js');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class SensorState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.tus = null;
      this.pillars = null;
      this.gfX = null;
      this.gfY = null;
      this.gfZ = null;
      this.gtX = null;
      this.gtY = null;
      this.gtZ = null;
      this.friction_est = null;
      this.target_grip_force = null;
      this.is_sd_active = null;
      this.is_ref_loaded = null;
      this.is_contact = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('tus')) {
        this.tus = initObj.tus
      }
      else {
        this.tus = 0;
      }
      if (initObj.hasOwnProperty('pillars')) {
        this.pillars = initObj.pillars
      }
      else {
        this.pillars = [];
      }
      if (initObj.hasOwnProperty('gfX')) {
        this.gfX = initObj.gfX
      }
      else {
        this.gfX = 0.0;
      }
      if (initObj.hasOwnProperty('gfY')) {
        this.gfY = initObj.gfY
      }
      else {
        this.gfY = 0.0;
      }
      if (initObj.hasOwnProperty('gfZ')) {
        this.gfZ = initObj.gfZ
      }
      else {
        this.gfZ = 0.0;
      }
      if (initObj.hasOwnProperty('gtX')) {
        this.gtX = initObj.gtX
      }
      else {
        this.gtX = 0.0;
      }
      if (initObj.hasOwnProperty('gtY')) {
        this.gtY = initObj.gtY
      }
      else {
        this.gtY = 0.0;
      }
      if (initObj.hasOwnProperty('gtZ')) {
        this.gtZ = initObj.gtZ
      }
      else {
        this.gtZ = 0.0;
      }
      if (initObj.hasOwnProperty('friction_est')) {
        this.friction_est = initObj.friction_est
      }
      else {
        this.friction_est = 0.0;
      }
      if (initObj.hasOwnProperty('target_grip_force')) {
        this.target_grip_force = initObj.target_grip_force
      }
      else {
        this.target_grip_force = 0.0;
      }
      if (initObj.hasOwnProperty('is_sd_active')) {
        this.is_sd_active = initObj.is_sd_active
      }
      else {
        this.is_sd_active = false;
      }
      if (initObj.hasOwnProperty('is_ref_loaded')) {
        this.is_ref_loaded = initObj.is_ref_loaded
      }
      else {
        this.is_ref_loaded = false;
      }
      if (initObj.hasOwnProperty('is_contact')) {
        this.is_contact = initObj.is_contact
      }
      else {
        this.is_contact = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SensorState
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [tus]
    bufferOffset = _serializer.int64(obj.tus, buffer, bufferOffset);
    // Serialize message field [pillars]
    // Serialize the length for message field [pillars]
    bufferOffset = _serializer.uint32(obj.pillars.length, buffer, bufferOffset);
    obj.pillars.forEach((val) => {
      bufferOffset = PillarState.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [gfX]
    bufferOffset = _serializer.float32(obj.gfX, buffer, bufferOffset);
    // Serialize message field [gfY]
    bufferOffset = _serializer.float32(obj.gfY, buffer, bufferOffset);
    // Serialize message field [gfZ]
    bufferOffset = _serializer.float32(obj.gfZ, buffer, bufferOffset);
    // Serialize message field [gtX]
    bufferOffset = _serializer.float32(obj.gtX, buffer, bufferOffset);
    // Serialize message field [gtY]
    bufferOffset = _serializer.float32(obj.gtY, buffer, bufferOffset);
    // Serialize message field [gtZ]
    bufferOffset = _serializer.float32(obj.gtZ, buffer, bufferOffset);
    // Serialize message field [friction_est]
    bufferOffset = _serializer.float32(obj.friction_est, buffer, bufferOffset);
    // Serialize message field [target_grip_force]
    bufferOffset = _serializer.float32(obj.target_grip_force, buffer, bufferOffset);
    // Serialize message field [is_sd_active]
    bufferOffset = _serializer.bool(obj.is_sd_active, buffer, bufferOffset);
    // Serialize message field [is_ref_loaded]
    bufferOffset = _serializer.bool(obj.is_ref_loaded, buffer, bufferOffset);
    // Serialize message field [is_contact]
    bufferOffset = _serializer.bool(obj.is_contact, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SensorState
    let len;
    let data = new SensorState(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [tus]
    data.tus = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [pillars]
    // Deserialize array length for message field [pillars]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.pillars = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.pillars[i] = PillarState.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [gfX]
    data.gfX = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [gfY]
    data.gfY = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [gfZ]
    data.gfZ = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [gtX]
    data.gtX = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [gtY]
    data.gtY = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [gtZ]
    data.gtZ = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [friction_est]
    data.friction_est = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [target_grip_force]
    data.target_grip_force = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [is_sd_active]
    data.is_sd_active = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [is_ref_loaded]
    data.is_ref_loaded = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [is_contact]
    data.is_contact = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    object.pillars.forEach((val) => {
      length += PillarState.getMessageSize(val);
    });
    return length + 47;
  }

  static datatype() {
    // Returns string type for a message object
    return 'papillarray_ros_v2/SensorState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5d7c28da3453a417882d03f775d18f22';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    int64 tus
    PillarState[] pillars
    float32 gfX
    float32 gfY
    float32 gfZ
    float32 gtX
    float32 gtY
    float32 gtZ
    float32 friction_est
    float32 target_grip_force
    bool is_sd_active
    bool is_ref_loaded
    bool is_contact
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    ================================================================================
    MSG: papillarray_ros_v2/PillarState
    Header header
    int32 id
    float32 dX
    float32 dY
    float32 dZ
    float32 fX
    float32 fY
    float32 fZ
    bool in_contact
    int32 slip_state
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SensorState(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.tus !== undefined) {
      resolved.tus = msg.tus;
    }
    else {
      resolved.tus = 0
    }

    if (msg.pillars !== undefined) {
      resolved.pillars = new Array(msg.pillars.length);
      for (let i = 0; i < resolved.pillars.length; ++i) {
        resolved.pillars[i] = PillarState.Resolve(msg.pillars[i]);
      }
    }
    else {
      resolved.pillars = []
    }

    if (msg.gfX !== undefined) {
      resolved.gfX = msg.gfX;
    }
    else {
      resolved.gfX = 0.0
    }

    if (msg.gfY !== undefined) {
      resolved.gfY = msg.gfY;
    }
    else {
      resolved.gfY = 0.0
    }

    if (msg.gfZ !== undefined) {
      resolved.gfZ = msg.gfZ;
    }
    else {
      resolved.gfZ = 0.0
    }

    if (msg.gtX !== undefined) {
      resolved.gtX = msg.gtX;
    }
    else {
      resolved.gtX = 0.0
    }

    if (msg.gtY !== undefined) {
      resolved.gtY = msg.gtY;
    }
    else {
      resolved.gtY = 0.0
    }

    if (msg.gtZ !== undefined) {
      resolved.gtZ = msg.gtZ;
    }
    else {
      resolved.gtZ = 0.0
    }

    if (msg.friction_est !== undefined) {
      resolved.friction_est = msg.friction_est;
    }
    else {
      resolved.friction_est = 0.0
    }

    if (msg.target_grip_force !== undefined) {
      resolved.target_grip_force = msg.target_grip_force;
    }
    else {
      resolved.target_grip_force = 0.0
    }

    if (msg.is_sd_active !== undefined) {
      resolved.is_sd_active = msg.is_sd_active;
    }
    else {
      resolved.is_sd_active = false
    }

    if (msg.is_ref_loaded !== undefined) {
      resolved.is_ref_loaded = msg.is_ref_loaded;
    }
    else {
      resolved.is_ref_loaded = false
    }

    if (msg.is_contact !== undefined) {
      resolved.is_contact = msg.is_contact;
    }
    else {
      resolved.is_contact = false
    }

    return resolved;
    }
};

module.exports = SensorState;

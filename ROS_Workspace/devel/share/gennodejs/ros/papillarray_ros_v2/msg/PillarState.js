// Auto-generated. Do not edit!

// (in-package papillarray_ros_v2.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class PillarState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.id = null;
      this.dX = null;
      this.dY = null;
      this.dZ = null;
      this.fX = null;
      this.fY = null;
      this.fZ = null;
      this.in_contact = null;
      this.slip_state = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = 0;
      }
      if (initObj.hasOwnProperty('dX')) {
        this.dX = initObj.dX
      }
      else {
        this.dX = 0.0;
      }
      if (initObj.hasOwnProperty('dY')) {
        this.dY = initObj.dY
      }
      else {
        this.dY = 0.0;
      }
      if (initObj.hasOwnProperty('dZ')) {
        this.dZ = initObj.dZ
      }
      else {
        this.dZ = 0.0;
      }
      if (initObj.hasOwnProperty('fX')) {
        this.fX = initObj.fX
      }
      else {
        this.fX = 0.0;
      }
      if (initObj.hasOwnProperty('fY')) {
        this.fY = initObj.fY
      }
      else {
        this.fY = 0.0;
      }
      if (initObj.hasOwnProperty('fZ')) {
        this.fZ = initObj.fZ
      }
      else {
        this.fZ = 0.0;
      }
      if (initObj.hasOwnProperty('in_contact')) {
        this.in_contact = initObj.in_contact
      }
      else {
        this.in_contact = false;
      }
      if (initObj.hasOwnProperty('slip_state')) {
        this.slip_state = initObj.slip_state
      }
      else {
        this.slip_state = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PillarState
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [id]
    bufferOffset = _serializer.int32(obj.id, buffer, bufferOffset);
    // Serialize message field [dX]
    bufferOffset = _serializer.float32(obj.dX, buffer, bufferOffset);
    // Serialize message field [dY]
    bufferOffset = _serializer.float32(obj.dY, buffer, bufferOffset);
    // Serialize message field [dZ]
    bufferOffset = _serializer.float32(obj.dZ, buffer, bufferOffset);
    // Serialize message field [fX]
    bufferOffset = _serializer.float32(obj.fX, buffer, bufferOffset);
    // Serialize message field [fY]
    bufferOffset = _serializer.float32(obj.fY, buffer, bufferOffset);
    // Serialize message field [fZ]
    bufferOffset = _serializer.float32(obj.fZ, buffer, bufferOffset);
    // Serialize message field [in_contact]
    bufferOffset = _serializer.bool(obj.in_contact, buffer, bufferOffset);
    // Serialize message field [slip_state]
    bufferOffset = _serializer.int32(obj.slip_state, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PillarState
    let len;
    let data = new PillarState(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [id]
    data.id = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [dX]
    data.dX = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [dY]
    data.dY = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [dZ]
    data.dZ = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [fX]
    data.fX = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [fY]
    data.fY = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [fZ]
    data.fZ = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [in_contact]
    data.in_contact = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [slip_state]
    data.slip_state = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 33;
  }

  static datatype() {
    // Returns string type for a message object
    return 'papillarray_ros_v2/PillarState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f75cd8df721a8e7158c9671c32de7f98';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PillarState(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = 0
    }

    if (msg.dX !== undefined) {
      resolved.dX = msg.dX;
    }
    else {
      resolved.dX = 0.0
    }

    if (msg.dY !== undefined) {
      resolved.dY = msg.dY;
    }
    else {
      resolved.dY = 0.0
    }

    if (msg.dZ !== undefined) {
      resolved.dZ = msg.dZ;
    }
    else {
      resolved.dZ = 0.0
    }

    if (msg.fX !== undefined) {
      resolved.fX = msg.fX;
    }
    else {
      resolved.fX = 0.0
    }

    if (msg.fY !== undefined) {
      resolved.fY = msg.fY;
    }
    else {
      resolved.fY = 0.0
    }

    if (msg.fZ !== undefined) {
      resolved.fZ = msg.fZ;
    }
    else {
      resolved.fZ = 0.0
    }

    if (msg.in_contact !== undefined) {
      resolved.in_contact = msg.in_contact;
    }
    else {
      resolved.in_contact = false
    }

    if (msg.slip_state !== undefined) {
      resolved.slip_state = msg.slip_state;
    }
    else {
      resolved.slip_state = 0
    }

    return resolved;
    }
};

module.exports = PillarState;

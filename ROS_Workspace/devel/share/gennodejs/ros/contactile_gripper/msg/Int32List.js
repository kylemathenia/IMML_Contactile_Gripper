// Auto-generated. Do not edit!

// (in-package contactile_gripper.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Int32List {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.list = null;
    }
    else {
      if (initObj.hasOwnProperty('list')) {
        this.list = initObj.list
      }
      else {
        this.list = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Int32List
    // Serialize message field [list]
    bufferOffset = _arraySerializer.int32(obj.list, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Int32List
    let len;
    let data = new Int32List(null);
    // Deserialize message field [list]
    data.list = _arrayDeserializer.int32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.list.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'contactile_gripper/Int32List';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '33cd48253e96459f6910f32d963eda83';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32[] list
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Int32List(null);
    if (msg.list !== undefined) {
      resolved.list = msg.list;
    }
    else {
      resolved.list = []
    }

    return resolved;
    }
};

module.exports = Int32List;

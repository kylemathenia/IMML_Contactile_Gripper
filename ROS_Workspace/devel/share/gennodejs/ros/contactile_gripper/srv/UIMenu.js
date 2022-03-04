// Auto-generated. Do not edit!

// (in-package contactile_gripper.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class UIMenuRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.menu = null;
    }
    else {
      if (initObj.hasOwnProperty('menu')) {
        this.menu = initObj.menu
      }
      else {
        this.menu = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type UIMenuRequest
    // Serialize message field [menu]
    bufferOffset = _serializer.string(obj.menu, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type UIMenuRequest
    let len;
    let data = new UIMenuRequest(null);
    // Deserialize message field [menu]
    data.menu = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.menu.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'contactile_gripper/UIMenuRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c203365aa9fc4c84f5cecbbb5ac3272a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string menu
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new UIMenuRequest(null);
    if (msg.menu !== undefined) {
      resolved.menu = msg.menu;
    }
    else {
      resolved.menu = ''
    }

    return resolved;
    }
};

class UIMenuResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type UIMenuResponse
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type UIMenuResponse
    let len;
    let data = new UIMenuResponse(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'contactile_gripper/UIMenuResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new UIMenuResponse(null);
    return resolved;
    }
};

module.exports = {
  Request: UIMenuRequest,
  Response: UIMenuResponse,
  md5sum() { return 'c203365aa9fc4c84f5cecbbb5ac3272a'; },
  datatype() { return 'contactile_gripper/UIMenu'; }
};

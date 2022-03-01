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

class DataRecorderRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.file_prefix = null;
      this.topic_list = null;
      this.stop = null;
    }
    else {
      if (initObj.hasOwnProperty('file_prefix')) {
        this.file_prefix = initObj.file_prefix
      }
      else {
        this.file_prefix = '';
      }
      if (initObj.hasOwnProperty('topic_list')) {
        this.topic_list = initObj.topic_list
      }
      else {
        this.topic_list = [];
      }
      if (initObj.hasOwnProperty('stop')) {
        this.stop = initObj.stop
      }
      else {
        this.stop = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type DataRecorderRequest
    // Serialize message field [file_prefix]
    bufferOffset = _serializer.string(obj.file_prefix, buffer, bufferOffset);
    // Serialize message field [topic_list]
    bufferOffset = _arraySerializer.string(obj.topic_list, buffer, bufferOffset, null);
    // Serialize message field [stop]
    bufferOffset = _serializer.bool(obj.stop, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DataRecorderRequest
    let len;
    let data = new DataRecorderRequest(null);
    // Deserialize message field [file_prefix]
    data.file_prefix = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [topic_list]
    data.topic_list = _arrayDeserializer.string(buffer, bufferOffset, null)
    // Deserialize message field [stop]
    data.stop = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.file_prefix.length;
    object.topic_list.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 9;
  }

  static datatype() {
    // Returns string type for a service object
    return 'contactile_gripper/DataRecorderRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '86296c4752d7ffaaedf71fd495fe5e5f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string file_prefix
    string[] topic_list
    bool stop
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new DataRecorderRequest(null);
    if (msg.file_prefix !== undefined) {
      resolved.file_prefix = msg.file_prefix;
    }
    else {
      resolved.file_prefix = ''
    }

    if (msg.topic_list !== undefined) {
      resolved.topic_list = msg.topic_list;
    }
    else {
      resolved.topic_list = []
    }

    if (msg.stop !== undefined) {
      resolved.stop = msg.stop;
    }
    else {
      resolved.stop = false
    }

    return resolved;
    }
};

class DataRecorderResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type DataRecorderResponse
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DataRecorderResponse
    let len;
    let data = new DataRecorderResponse(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'contactile_gripper/DataRecorderResponse';
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
    const resolved = new DataRecorderResponse(null);
    return resolved;
    }
};

module.exports = {
  Request: DataRecorderRequest,
  Response: DataRecorderResponse,
  md5sum() { return '86296c4752d7ffaaedf71fd495fe5e5f'; },
  datatype() { return 'contactile_gripper/DataRecorder'; }
};

/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:17 2016. */

#ifndef PB_VEHICLE_GPS_POSITION_PB_H_INCLUDED
#define PB_VEHICLE_GPS_POSITION_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _px4_vehicle_gps_position_pb {
    uint64_t timestamp;
    uint64_t time_utc_usec;
    int32_t lat;
    int32_t lon;
    int32_t alt;
    int32_t alt_ellipsoid;
    float s_variance_m_s;
    float c_variance_rad;
    float eph;
    float epv;
    float hdop;
    float vdop;
    int32_t noise_per_ms;
    int32_t jamming_indicator;
    float vel_m_s;
    float vel_n_m_s;
    float vel_e_m_s;
    float vel_d_m_s;
    float cog_rad;
    int32_t timestamp_time_relative;
    uint32_t fix_type;
    bool vel_ned_valid;
    uint32_t satellites_used;
/* @@protoc_insertion_point(struct:px4_vehicle_gps_position_pb) */
} px4_vehicle_gps_position_pb;

/* Default values for struct fields */

/* Initializer values for message structs */
#define px4_vehicle_gps_position_pb_init_default {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
#define px4_vehicle_gps_position_pb_init_zero    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}

/* Field tags (for use in manual encoding/decoding) */
#define px4_vehicle_gps_position_pb_timestamp_tag 1
#define px4_vehicle_gps_position_pb_time_utc_usec_tag 2
#define px4_vehicle_gps_position_pb_lat_tag      3
#define px4_vehicle_gps_position_pb_lon_tag      4
#define px4_vehicle_gps_position_pb_alt_tag      5
#define px4_vehicle_gps_position_pb_alt_ellipsoid_tag 6
#define px4_vehicle_gps_position_pb_s_variance_m_s_tag 7
#define px4_vehicle_gps_position_pb_c_variance_rad_tag 8
#define px4_vehicle_gps_position_pb_eph_tag      9
#define px4_vehicle_gps_position_pb_epv_tag      10
#define px4_vehicle_gps_position_pb_hdop_tag     11
#define px4_vehicle_gps_position_pb_vdop_tag     12
#define px4_vehicle_gps_position_pb_noise_per_ms_tag 13
#define px4_vehicle_gps_position_pb_jamming_indicator_tag 14
#define px4_vehicle_gps_position_pb_vel_m_s_tag  15
#define px4_vehicle_gps_position_pb_vel_n_m_s_tag 16
#define px4_vehicle_gps_position_pb_vel_e_m_s_tag 17
#define px4_vehicle_gps_position_pb_vel_d_m_s_tag 18
#define px4_vehicle_gps_position_pb_cog_rad_tag  19
#define px4_vehicle_gps_position_pb_timestamp_time_relative_tag 20
#define px4_vehicle_gps_position_pb_fix_type_tag 21
#define px4_vehicle_gps_position_pb_vel_ned_valid_tag 22
#define px4_vehicle_gps_position_pb_satellites_used_tag 23

/* Struct field encoding specification for nanopb */
extern const pb_field_t px4_vehicle_gps_position_pb_fields[24];

/* Maximum encoded size of messages (where known) */
#define px4_vehicle_gps_position_pb_size         176

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define VEHICLE_GPS_POSITION_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif
/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:11 2016. */

#ifndef PB_FOLLOW_TARGET_PB_H_INCLUDED
#define PB_FOLLOW_TARGET_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _px4_follow_target_pb {
    uint64_t timestamp;
    double lat;
    double lon;
    float alt;
    float vy;
    float vx;
    float vz;
    uint32_t est_cap;
/* @@protoc_insertion_point(struct:px4_follow_target_pb) */
} px4_follow_target_pb;

/* Default values for struct fields */

/* Initializer values for message structs */
#define px4_follow_target_pb_init_default        {0, 0, 0, 0, 0, 0, 0, 0}
#define px4_follow_target_pb_init_zero           {0, 0, 0, 0, 0, 0, 0, 0}

/* Field tags (for use in manual encoding/decoding) */
#define px4_follow_target_pb_timestamp_tag       1
#define px4_follow_target_pb_lat_tag             2
#define px4_follow_target_pb_lon_tag             3
#define px4_follow_target_pb_alt_tag             4
#define px4_follow_target_pb_vy_tag              5
#define px4_follow_target_pb_vx_tag              6
#define px4_follow_target_pb_vz_tag              7
#define px4_follow_target_pb_est_cap_tag         8

/* Struct field encoding specification for nanopb */
extern const pb_field_t px4_follow_target_pb_fields[9];

/* Maximum encoded size of messages (where known) */
#define px4_follow_target_pb_size                55

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define FOLLOW_TARGET_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif
/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:07 2016. */

#ifndef PB_AIRSPEED_PB_H_INCLUDED
#define PB_AIRSPEED_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _px4_airspeed_pb {
    uint64_t timestamp;
    float indicated_airspeed_m_s;
    float true_airspeed_m_s;
    float true_airspeed_unfiltered_m_s;
    float air_temperature_celsius;
    float confidence;
/* @@protoc_insertion_point(struct:px4_airspeed_pb) */
} px4_airspeed_pb;

/* Default values for struct fields */

/* Initializer values for message structs */
#define px4_airspeed_pb_init_default             {0, 0, 0, 0, 0, 0}
#define px4_airspeed_pb_init_zero                {0, 0, 0, 0, 0, 0}

/* Field tags (for use in manual encoding/decoding) */
#define px4_airspeed_pb_timestamp_tag            1
#define px4_airspeed_pb_indicated_airspeed_m_s_tag 2
#define px4_airspeed_pb_true_airspeed_m_s_tag    3
#define px4_airspeed_pb_true_airspeed_unfiltered_m_s_tag 4
#define px4_airspeed_pb_air_temperature_celsius_tag 5
#define px4_airspeed_pb_confidence_tag           6

/* Struct field encoding specification for nanopb */
extern const pb_field_t px4_airspeed_pb_fields[7];

/* Maximum encoded size of messages (where known) */
#define px4_airspeed_pb_size                     36

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define AIRSPEED_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif
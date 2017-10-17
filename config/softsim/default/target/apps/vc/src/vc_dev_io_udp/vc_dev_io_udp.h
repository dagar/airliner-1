/****************************************************************************
*
*   Copyright (c) 2017 Windhover Labs, L.L.C. All rights reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions
* are met:
*
* 1. Redistributions of source code must retain the above copyright
*    notice, this list of conditions and the following disclaimer.
* 2. Redistributions in binary form must reproduce the above copyright
*    notice, this list of conditions and the following disclaimer in
*    the documentation and/or other materials provided with the
*    distribution.
* 3. Neither the name Windhover Labs nor the names of its 
*    contributors may be used to endorse or promote products derived 
*    from this software without specific prior written permission.
*
* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
* "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
* LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
* FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
* COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
* INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
* BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
* OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
* AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
* LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
* ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
* POSSIBILITY OF SUCH DAMAGE.
*
*****************************************************************************/

#ifndef VC_DEV_IO_UDP_H
#define VC_DEV_IO_UDP_H

#include "cfe.h"
#include "vc_dev_io.h"
#include "../vc_custom_shared.h"
#include "vc_perfids.h"
#include "vc_app.h"

/************************************************************************
** Local Defines
*************************************************************************/
/* TODO move to platform config */
/** \brief Size of the Gstreamer multipartmux preamble when configured
**         with a boundary = "*".
**
**  \par Limits:
**       Varies with boundary specified.
*/
#define VC_MPARTMUX_HEADER_SIZE 61
/** \brief Char count where length of the payload is specified in the 
**         multipartmux preamble.
*/
#define VC_MPARTMUX_HEADER_LENGTH_START 51

/************************************************************************
** Structure Declarations
*************************************************************************/

/**
 * Device modes
 */
typedef enum
{
    /*! Device state unused  */
    VC_DEVICE_UNUSED       = 0,
    /*! Device state disabled */
    VC_DEVICE_DISABLED     = 1,
    /*! Device state enabled */
    VC_DEVICE_ENABLED      = 2
} VC_DeviceMode_t;


/**
 * Device status
 */
typedef enum
{
    /*! Device status uninitialized */
    VC_DEVICE_UNINITIALIZED = 0,
    /*! Device status uninitialized */
    VC_DEVICE_INITIALIZED   = 1,
    /*! Device status streaming */
    VC_DEVICE_STREAMING     = 2
} VC_DeviceStatus_t;


/**
 * Device handle
 */
typedef struct
{
    /*! Device status */
    VC_DeviceStatus_t   Status;
    /*! Device mode */
    VC_DeviceMode_t     Mode;
    /*! Device socket file descriptor */
    int                 Socket;
    /*! Device port number */
    uint16              Port;
    /*! Device buffer for receiving image data */
    char Buffer[VC_MAX_PACKET_SIZE];
} VC_Device_Handle_t;


/**
 * Global data structure for custom device IO layer
 */
typedef struct
{
    /*! Flag to start and stop streaming */
    boolean                         ContinueFlag;
    /*! Streaming task priority */
    uint8                           Priority;
    /*! Streaming child task identifier */
    uint32                          ChildTaskID;
    /*! Streaming task function pointer */
    CFE_ES_ChildTaskMainFuncPtr_t   StreamingTask;
    /*! Device resource(s) channels */
    VC_Device_Handle_t              Channel[VC_MAX_DEVICES];
} VC_AppCustomDevice_t;


int32 VC_CleanupDevices(void);
int32 VC_Init_CustomDevices(void);
void VC_Stream_Task(void);
int32 VC_Send_Buffer(uint8 DeviceID);

#endif

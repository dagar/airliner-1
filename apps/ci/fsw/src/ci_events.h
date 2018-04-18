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

#ifndef CI_EVENTS_H
#define CI_EVENTS_H

#include <termio.h>
#include <stdlib.h>

#ifdef __cplusplus
extern "C" {
#endif

/************************************************************************
** Local Defines
*************************************************************************/


/* Event IDs
 * Conventions: _EID is the event identifier.  _EVT_CNT is the total number of
 * events and should always be last.  Events can be added before _EVT_CNT.
 * For long-term maintenance, consider not removing an event but replacing it
 * with an unused, reserved, enum to preserve the IDs later in the list. */
typedef enum {

/** \brief <tt> Value of zero is reserved, and should not be used. </tt> */
    CI_RESERVED_EID = 0,  /* Do not use this event ID */

/** \brief <tt> 'CI - ' </tt>
**  \event <tt> 'CI - ' </tt>
**  
**  \par Type: INFORMATION
**
**  \par Cause:
**
**  TODO fill this in
**
*/
    CI_INF_EID,

/** \brief <tt> 'CI Initialized. Version \%d.\%d.\%d' </tt>
**  \event <tt> 'CI Initialized. Version \%d.\%d.\%d' </tt>
**  
**  \par Type: INFORMATION
**
**  \par Cause:
**
**  This event message is issued when the CFS CI Task has
**  completed initialization.
**
**  The first \c %d field contains the Application's Major Version Number
**  The second \c %d field contains the Application's Minor Version Number
**  The third \c %d field contains the Application's Revision Number
*/
    CI_INIT_INF_EID,

/** \brief <tt> 'CI - ' </tt>
**  \event <tt> 'CI - ' </tt>
**  
**  \par Type: INFORMATION
**
**  \par Cause:
**
**  This message is generated when a table is initialized.
**
*/
    CI_CONFIG_TABLE_INF_EID,

/** \brief <tt> 'CI - ' </tt>
**  \event <tt> 'CI - ' </tt>
**  
**  \par Type: INFORMATION
**
**  \par Cause:
**
**  This event message is issued when TBD
**
*/
    CI_CDS_INF_EID,

/** \brief <tt> 'CI - Recvd $x cmd (%us)' </tt>
**  \event <tt> 'CI - Recvd $x cmd (%us)' </tt>
**  
**  \par Type: INFORMATION
**
**  \par Cause:
**
**  This event message is issued when the CFS CI Task has
**  received and processed a command.
**
*/
    CI_CMD_INF_EID,

/** \brief <tt> 'CI - ' </tt>
**  \event <tt> 'CI - ' </tt>
**  
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when TBD
**
*/
    CI_ERR_EID,

/** \brief <tt> 'CI - ' </tt>
**  \event <tt> 'CI - ' </tt>
**  
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when the CFS CI Task has
**  had an error in initialization.
**
*/
    CI_INIT_ERR_EID,

/** \brief <tt> 'CI - ' </tt>
**  \event <tt> 'CI - ' </tt>
**  
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when the CFS CI Task has
**  had an error with the configuration table.
**
*/
    CI_CONFIG_TABLE_ERR_EID,

/** \brief <tt> 'CI - ' </tt>
**  \event <tt> 'CI - ' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when the CFS CI Task has
**  had an error with the timeout table.
**
*/
	CI_TIMEOUT_TABLE_ERR_EID,

/** \brief <tt> 'CI - ' </tt>
**  \event <tt> 'CI - ' </tt>
**  
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when the CFS CI Task has
**  had an error in CDS.
**
*/
    CI_CDS_ERR_EID,

/** \brief <tt> 'CI - $commandError' </tt>
**  \event <tt> 'CI - $commandError' </tt>
**  
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when the CFS CI Task has
**  had an error processing a command.
**
*/
    CI_CMD_ERR_EID,

/** \brief <tt> 'CI: SB pipe read error (0x%08X), app will exit' </tt>
**  \event <tt> 'CI: SB pipe read error (0x%08X), app will exit' </tt>
**  
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when the CFS CI Task has
**  had an error reading from a pipe.
**
*/
    CI_PIPE_ERR_EID,

/** \brief <tt> 'CI - Recvd invalid $type msgId (0x%04x)' </tt>
**  \event <tt> 'CI - Recvd invalid $type msgId (0x%04x)' </tt>
**  
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when the CFS CI Task has
**  received an invalid message ID.
**
*/
    CI_MSGID_ERR_EID,

/** \brief <tt> 'CI - Rcvd invalid msgLen: msgId=0x%08X, cmdCode=%d, msgLen=%d, expectedLen=%d" </tt>
**  \event <tt> 'CI - Rcvd invalid msgLen: msgId=0x%08X, cmdCode=%d, msgLen=%d, expectedLen=%d" </tt>
**  
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when the CFS CI Task has
**  received a message with a bad length.
**
*/
    CI_MSGLEN_ERR_EID,

/** \brief <tt> 'CI - Listener child task failed.  CFE_ES_CreateChildTask returned: 0x%08X' </tt>
**  \event <tt> 'CI - Listener child task failed.  CFE_ES_CreateChildTask returned: 0x%08X' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when CI has failed to
**  create its child listener task.
**
*/
    CI_LISTENER_CREATE_CHDTASK_ERR_EID,

/** \brief <tt> 'CI - L%d, cmd %0x %0x dropped, too long' </tt>
**  \event <tt> 'CI - L%d, cmd %0x %0x dropped, too long' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when CI's listener thread
**  received a msg greater than the max allowed size.
**
*/
    CI_CMD_INGEST_ERR_EID,

/** \brief <tt> 'CI - Bind socket failed = %d' </tt>
**  \event <tt> 'CI - Bind socket failed = %d' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when the CI listener
**  encounters an error connecting to a socket.
**
*/
	CI_SOCKET_ERR_EID,

/** \brief <tt> 'CI - UDP command input enabled on port %u.' </tt>
**  \event <tt> 'CI - UDP command input enabled on port %u.' </tt>
**
**  \par Type: INFORMATION
**
**  \par Cause:
**
**  This event message is issued when the CI listener
**  successfully binds to a socket.
**
*/
	CI_ENA_INF_EID,

/** \brief <tt> 'CI - Rcvd invalid cmd' </tt>
**  \event <tt> 'CI - Rcvd invalid cmd' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when the CFS CI Task has
**  encountered an issue with a received command.
**
*/
	CI_CMD_INVALID_EID,

/** \brief <tt> 'CI - Cmd not authorized' </tt>
**  \event <tt> 'CI - Cmd not authorized' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when the command CI has
**  received is not authorized to execute.
**
*/
	CI_CMD_UNAUTHORIZED_EID,

/** \brief <tt> 'CI - Cmd authorization timeout' </tt>
**  \event <tt> 'CI - Cmd authorization timeout' </tt>
**
**  \par Type: INFORMATION
**
**  \par Cause:
**
**  This event message is issued when an authorized
**  command has timed out.
**
*/
	CI_CMD_AUTH_TIMEOUT_EID,

/** \brief <tt> 'CI - Cmd not registered' </tt>
**  \event <tt> 'CI - Cmd not registered' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when attempting to
**  authorize a command that is not registered.
**
*/
	CI_CMD_AUTH_NOT_REG_EID,

/** \brief <tt> 'CI - Cmd not 2-step' </tt>
**  \event <tt> 'CI - Cmd not 2-step' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when attempting to
**  authorize a command that is not 2-step.
**
*/
	CI_CMD_AUTH_INV_MODE_EID,

/** \brief <tt> 'CI - Cmd already authorized' </tt>
**  \event <tt> 'CI - Cmd already authorized' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when attempting to
**  authorize a command that is already authorized.
**
*/
	CI_CMD_AUTH_INV_STATE_EID,

/** \brief <tt> 'CI - Cmd authorized' </tt>
**  \event <tt> 'CI - Cmd authorized' </tt>
**
**  \par Type: INFORMATION
**
**  \par Cause:
**
**  This event message is issued when a command is authorized.
**
*/
	CI_CMD_AUTHORIZED_EID,

/** \brief <tt> 'CI - Cmd not registered' </tt>
**  \event <tt> 'CI - Cmd not registered' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when a command
**  is not registered.
**
*/
	CI_CMD_DEAUTH_NOT_REG_EID,

/** \brief <tt> 'CI - Cmd not 2-step' </tt>
**  \event <tt> 'CI - Cmd not 2-step' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when attempting to
**  deauthorize a command that is not 2-step.
**
*/
	CI_CMD_DEAUTH_INV_MODE_EID,

/** \brief <tt> 'CI - Cmd not authorized' </tt>
**  \event <tt> 'CI - Cmd not authorized' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when attempting to
**  deauthorize a command that is not authorized.
**
*/
	CI_CMD_DEAUTH_INV_STATE_EID,

/** \brief <tt> 'CI - Cmd deauthorized' </tt>
**  \event <tt> 'CI - Cmd deauthorized' </tt>
**
**  \par Type: INFORMATION
**
**  \par Cause:
**
**  This event message is issued when a command is deauthorized.
**
*/
	CI_CMD_DEAUTHORIZED_EID,

/** \brief <tt> 'CI - Cmd registered' </tt>
**  \event <tt> 'CI - Cmd registered' </tt>
**
**  \par Type: INFORMATION
**
**  \par Cause:
**
**  This event message is issued when a command is registered.
**
*/
	CI_CMD_REGISTERED_EID,

/** \brief <tt> 'CI - Cmd already registered' </tt>
**  \event <tt> 'CI - Cmd already registered' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when attempting to register
**  a command that is already registered.
**
*/
	CI_CMD_ALREADY_REGISTERED_EID,

/** \brief <tt> 'CI - Cmd deregistered' </tt>
**  \event <tt> 'CI - Cmd deregistered' </tt>
**
**  \par Type: INFORMATION
**
**  \par Cause:
**
**  This event message is issued when a command is deregistered.
**
*/
	CI_CMD_DEREGISTERED_EID,

/** \brief <tt> 'CI - Cmd not registered' </tt>
**  \event <tt> 'CI - Cmd not registered' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when attempting to deregister
**  a command that is not registered.
**
*/
	CI_CMD_NOT_REGISTERED_EID,

/** \brief <tt> 'CI - Unable to register cmd' </tt>
**  \event <tt> 'CI - Unable to register cmd' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when attempting to register
**  a command and an error is encountered.
**
*/
	CI_CMD_REG_ERR_EID,

/** \brief <tt> 'CI - Invalid state of command to update' </tt>
**  \event <tt> 'CI - Invalid state of command to update' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when attempting to update
**  a 2-step registered command while it is authorized
*/
	CI_CMD_UPDT_REG_INVLD_STATE_EID,

/** \brief <tt> 'CI - Cmd updated' </tt>
**  \event <tt> 'CI - Cmd updated' </tt>
**
**  \par Type: INFORMATION
**
**  \par Cause:
**
**  This event message is issued when a command registration is updated.
**
*/
	CI_CMD_UPDATE_REG_EID,

/** \brief <tt> 'CI - Unable to find deserialization function' </tt>
**  \event <tt> 'CI - Unable to find deserialization function' </tt>
**
**  \par Type: ERROR
**
**  \par Cause:
**
**  This event message is issued when CI receives a message
**  that requires deserialization and it is unable to locate
**  that message's decoding function
*/
	CI_NO_DECODE_FUNC_EID,

/** \brief <tt> This is a count of all the app events and should not be used. </tt> */
    CI_EVT_CNT
} CI_EventIds_t;


#ifdef __cplusplus
}
#endif

#endif /* CI_EVENTS_H */

/************************/
/*  End of File Comment */
/************************/
    

/************************************************************************
** Pragmas
*************************************************************************/

/************************************************************************
** Includes
*************************************************************************/
#include "cfe_tbl_filedef.h"
#include "to_tbldefs.h"
#include "msg_ids.h"

/************************************************************************
** Local Defines
*************************************************************************/

/************************************************************************
** Local Structure Definitions
*************************************************************************/

/**
** \brief The cFE TO config table definition.
**
** Content format: ObjName[64], TblName[38], Desc[32], TgtFileName[20], ObjSize
**    ObjName - variable name of config table, e.g., TO_ConfigDefTbl[]
**    TblName - app's table name, e.g., TO.CONFIG_TBL, where TO is the same app name
**              used in cfe_es_startup.scr, and TO_defConfigTbl is the same table
**              name passed in to CFE_TBL_Register()
**    Desc - description of table in string format
**    TgtFileName[20] - table file name, compiled as .tbl file extension
**    ObjSize - size of the entire table
**
*/
static CFE_TBL_FileDef_t CFE_TBL_FileDef =
{
    "TO_ConfigTbl", "TO.CONFIG_TBL", "TO default config table",
    "to_config.tbl", (sizeof(TO_ConfigTbl_t))
};

/************************************************************************
** External Global Variables
*************************************************************************/

/************************************************************************
** Global Variables
*************************************************************************/

#define TO_PQUEUE_GROUND_SINGLE_PASS_IDX		0
#define TO_PQUEUE_GROUND_HIGH_OPS_RSRVD_IDX		1
#define TO_PQUEUE_GROUND_HIGH_IDX				2
#define TO_PQUEUE_GROUND_MEDIUM_IDX				3
#define TO_PQUEUE_GROUND_LOW_IDX				4
#define TO_PQUEUE_ONBOARD_SINGLE_PASS_IDX		5
#define TO_PQUEUE_ONBOARD_HIGH_OPS_RSRVD_IDX	6
#define TO_PQUEUE_ONBOARD_HIGH_IDX				7
#define TO_PQUEUE_ONBOARD_MEDIUM_IDX			8
#define TO_PQUEUE_ONBOARD_LOW_IDX				9

#define TO_CHANNEL_GROUND						0
#define TO_CHANNEL_ONBOARD						1

/**
**  \brief Default TO config table data
*/
TO_ConfigTbl_t TO_ConfigTbl =
{
	/* Table ID */
	1,
	{
		/* Message Flows */
		/* Ground Queues */
		{CFE_ES_HK_TLM_MID,			1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CFE_EVS_HK_TLM_MID,		1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CFE_SB_HK_TLM_MID,			1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CFE_TBL_HK_TLM_MID,		1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CFE_TIME_HK_TLM_MID,		1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CFE_TIME_DIAG_TLM_MID,		1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CFE_EVS_EVENT_MSG_MID,		32, TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CFE_SB_STATS_TLM_MID,		1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CFE_ES_APP_TLM_MID,		1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CFE_TBL_REG_TLM_MID,		1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CFE_SB_ONESUB_TLM_MID,		1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CFE_ES_SHELL_TLM_MID,		32, TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CFE_ES_MEMSTATS_TLM_MID,	1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CF_HK_TLM_MID,				1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CF_TRANS_TLM_MID,			1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CF_CONFIG_TLM_MID,			1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CF_SPACE_TO_GND_PDU_MID,	32,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CS_HK_TLM_MID,				1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{DS_HK_TLM_MID,				1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{DS_DIAG_TLM_MID,			1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{FM_HK_TLM_MID,				1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{FM_FILE_INFO_TLM_MID,		1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{FM_DIR_LIST_TLM_MID,		1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{FM_OPEN_FILES_TLM_MID,		1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{FM_FREE_SPACE_TLM_MID,		1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{HK_HK_TLM_MID,				1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{HS_HK_TLM_MID,				1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{LC_HK_TLM_MID,				1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{MD_HK_TLM_MID,				1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{MM_HK_TLM_MID,				1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{SCH_HK_TLM_MID,			1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{SCH_DIAG_TLM_MID,			1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{CI_HK_TLM_MID,				1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{TO_HK_TLM_MID,				1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},
		{TO_DATA_TYPE_MID,			1,	TO_PQUEUE_GROUND_MEDIUM_IDX, 0, 0, 0},

		/* Onboard Queues */
		{CFE_ES_HK_TLM_MID,			1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CFE_EVS_HK_TLM_MID,		1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CFE_SB_HK_TLM_MID,			1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CFE_TBL_HK_TLM_MID,		1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CFE_TIME_HK_TLM_MID,		1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CFE_TIME_DIAG_TLM_MID,		1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CFE_EVS_EVENT_MSG_MID,		32, TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CFE_SB_STATS_TLM_MID,		1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CFE_ES_APP_TLM_MID,		1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CFE_TBL_REG_TLM_MID,		1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CFE_SB_ONESUB_TLM_MID,		1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CFE_ES_SHELL_TLM_MID,		32, TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CFE_ES_MEMSTATS_TLM_MID,	1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CF_HK_TLM_MID,				1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CF_TRANS_TLM_MID,			1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CF_CONFIG_TLM_MID,			1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CF_SPACE_TO_GND_PDU_MID,	32,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CS_HK_TLM_MID,				1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{DS_HK_TLM_MID,				1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{DS_DIAG_TLM_MID,			1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{FM_HK_TLM_MID,				1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{FM_FILE_INFO_TLM_MID,		1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{FM_DIR_LIST_TLM_MID,		1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{FM_OPEN_FILES_TLM_MID,		1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{FM_FREE_SPACE_TLM_MID,		1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{HK_HK_TLM_MID,				1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{HS_HK_TLM_MID,				1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{LC_HK_TLM_MID,				1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{MD_HK_TLM_MID,				1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{MM_HK_TLM_MID,				1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{SCH_HK_TLM_MID,			1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{SCH_DIAG_TLM_MID,			1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{CI_HK_TLM_MID,				1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{TO_HK_TLM_MID,				1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
		{TO_DATA_TYPE_MID,			1,	TO_PQUEUE_ONBOARD_MEDIUM_IDX, 0, 0, 0},
	},{
		/* Priority Queues */
		/* TO_PQUEUE_GROUND_SINGLE_PASS_IDX */
		{TO_PQUEUE_ENA, TO_CHANNEL_GROUND, 10, TO_PRIORITY_QUEUE_TYPE_SINGLE, 0, 0},
		/* TO_PQUEUE_GROUND_HIGH_OPS_RSRVD_IDX */
		{TO_PQUEUE_ENA, TO_CHANNEL_GROUND, 10, TO_PRIORITY_QUEUE_TYPE_FIFO, 0, 0},
		/* TO_PQUEUE_GROUND_HIGH_IDX */
		{TO_PQUEUE_ENA, TO_CHANNEL_GROUND, 10, TO_PRIORITY_QUEUE_TYPE_FIFO, 0, 0},
		/* TO_PQUEUE_GROUND_MEDIUM_IDX */
		{TO_PQUEUE_ENA, TO_CHANNEL_GROUND, 10, TO_PRIORITY_QUEUE_TYPE_FIFO, 0, 0},
		/* TO_PQUEUE_GROUND_LOW_IDX */
		{TO_PQUEUE_ENA, TO_CHANNEL_GROUND, 10, TO_PRIORITY_QUEUE_TYPE_FIFO, 0, 0},
		/* TO_PQUEUE_ONBOARD_SINGLE_PASS_IDX */
		{TO_PQUEUE_ENA, TO_CHANNEL_ONBOARD, 10, TO_PRIORITY_QUEUE_TYPE_SINGLE, 0, 0},
		/* TO_PQUEUE_GROUND_HIGH_OPS_RSRVD_IDX */
		{TO_PQUEUE_ENA, TO_CHANNEL_ONBOARD, 10, TO_PRIORITY_QUEUE_TYPE_FIFO, 0, 0},
		/* TO_PQUEUE_GROUND_HIGH_IDX */
		{TO_PQUEUE_ENA, TO_CHANNEL_ONBOARD, 10, TO_PRIORITY_QUEUE_TYPE_FIFO, 0, 0},
		/* TO_PQUEUE_GROUND_MEDIUM_IDX */
		{TO_PQUEUE_ENA, TO_CHANNEL_ONBOARD, 10, TO_PRIORITY_QUEUE_TYPE_FIFO, 0, 0},
		/* TO_PQUEUE_GROUND_LOW_IDX */
		{TO_PQUEUE_ENA, TO_CHANNEL_ONBOARD, 10, TO_PRIORITY_QUEUE_TYPE_FIFO, 0, 0},
	},
	{
		/* Output Channels */
		/* TO_CHANNEL_GROUND */
		{TO_OUT_CHANNEL_ENA, 10, 0, 0, 0},
		/* TO_CHANNEL_ONBOARD */
		{TO_OUT_CHANNEL_ENA, 10, 0, 0, 0}
	}
};

/************************************************************************
** Local Variables
*************************************************************************/

/************************************************************************
** Local Function Prototypes
*************************************************************************/

/************************************************************************
** Function Definitions
*************************************************************************/

/************************/
/*  End of File Comment */
/************************/
    

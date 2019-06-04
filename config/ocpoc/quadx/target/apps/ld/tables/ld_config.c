/*
** Pragmas
*/

/*
** Include Files
*/
#include "cfe_tbl_filedef.h"
#include "ld_tbldefs.h"

/*
** Local Defines
*/

/*
** Local Structure Declarations
*/
static OS_USED CFE_TBL_FileDef_t CFE_TBL_FileDef =
{
    /* Content format: ObjName[64], TblName[38], Desc[32], TgtFileName[20], ObjSize
    **    ObjName - variable name of config table, e.g., CI_ConfigDefTbl[]
    **    TblName - app's table name, e.g., CI.CONFIG_TBL, where CI is the same app name
    **              used in cfe_es_startup.scr, and CI_defConfigTbl is the same table
    **              name passed in to CFE_TBL_Register()
    **    Desc - description of table in string format
    **    TgtFileName[20] - table file name, compiled as .tbl file extension
    **    ObjSize - size of the entire table
    */

    "LD_ConfigTbl", "LD.CONFIG_TBL", "LD default config table",
    "ld_config.tbl", (sizeof(LD_ConfigTbl_t))
};

/*
** External Global Variables
*/

/*
** Global Variables
*/

/* Default ULR config table data */
LD_ConfigTbl_t LD_ConfigTbl =
{
	    /** \brief Multicopter max climb rate.
	     *
	     *  \par Limits:
	     *  	default 0.5.
	     */
	    0.5,

	    /** \brief Multicopter max horizontal velocity.
	     *
	     *  \par Limits:
	     *  	default 1.5.
	     */
	    1.50,

	    /** \brief Multicopter max rotation.
	     *
	     *  \par Limits:
	     *  	default 20.0.
	     */
	    20.0,

	    /** \brief Multicopter specific force threshold.
	     *
	     *  \par Limits:
	     *  	Min > Max (incr.) 0.1 > 10 , default 2.0.
	     */
	    2.0,

	    /** \brief Multicopter sub-hover throttle scaling.
	     *
	     *  \par Limits:
	     *  	Min > Max (incr.) 0.05 > 0.5 , default 0.1.
	     */
	    0.5,

	    /** \brief Multicopter free-fall trigger time.
	     *
	     *  \par Limits:
	     *  	Min > Max (incr.) 0.02 > 5 , default 0.3.
	     */
	    0.3,

	    /** \brief Multicopter Flight stick down threshold for landing.
	     *
	     *  \par Limits:
	     *  	default 0.15.
	     */
	    0.15,

	    /** \brief Multicopter Flight stick up threshold for take off.
	     *
	     *  \par Limits:
	     *  	default 0.65.
	     */
	    0.65,

	    /** \brief Total flight time in ms, higher 32 bits of the value.
	     *
	     *  \par Limits:
	     *  	default 0.
	     */
	    0,

	    /** \brief Total flight time in ms, lower 32 bits of the value.
	     *
	     *  \par Limits:
	     *  	default 60299599.
	     */
		60299599,

	    /** \brief Multicopter maximum altitude.
	     *
	     *  \par Limits:
	     *  	default 10000.0.
	     */
	    10000.0,

	    /** \brief Multicopter minimum throttle.
	     *
	     *  \par Limits:
	     *  	default 0.12.
	     */
	    0.12,

	    /** \brief Multicopter hover throttle.
	     *
	     *  \par Limits:
	     *  	default 0.5.
	     */
	    0.65,

	    /** \brief Multicopter throttle range.
	     *
	     *  \par Limits:
	     *  	default 0.1.
	     */
	    0.5,

	    /** \brief Multicopter minimum throttle in manual mode.
	     *
	     *  \par Limits:
	     *  	default 0.08.
	     */
	   0.08,

	    /** \brief Multicopter takeoff stick up threshold in position control mode.
	     *
	     *  \par Limits:
	     *  	default 0.65.
	     */
	    0.65,

	    /** \brief Multicopter takeoff stick down threshold in position control mode.
	     *
	     *  \par Limits:
	     *  	default 0.15.
	     */
	    0.15,

        /** \brief Landing descend rate.
         *
         *  \par Limits:
         *      default 0.5.
         */
        0.3f
};

/*
** Local Variables
*/

/*
** Function Prototypes
*/

/*
** Function Definitions
*/

/*=======================================================================================
** End of file ld_config.c
**=====================================================================================*/
    

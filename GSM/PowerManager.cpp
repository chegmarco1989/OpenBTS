/* GSM/PowerManager.cpp */
/*-
 * Copyright 2009 Free Software Foundation, Inc.
 * Copyright 2014 Range Networks, Inc.
 *
 * This software is distributed under multiple licenses;
 * see the COPYING file in the main directory for licensing
 * information for this specific distribution.
 *
 * This use of this software may be subject to additional restrictions.
 * See the LEGAL file in the main directory for details.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 */

#include <CommonLibs/Logger.h>
#include <Control/ControlCommon.h>
#include <TRXManager/TRXManager.h>
#include <apps/OpenBTSConfig.h>

#include "GSMConfig.h"
#include "PowerManager.h"

#define LOG_GROUP LogGroup::GSM // Can set Log.Level.GSM for debugging

namespace GSM {

PowerManager gPowerManager;

void PowerManager::pmSetAttenDirect(int atten)
{
	mRadio->setPower(atten);
	mAtten = atten;
	LOG(INFO) << "setting power to -" << mAtten << " dB at uptime=" << gBTS->uptime();
}

void PowerManager::pmSetAtten(int atten)
{
	if (atten != mAtten) {
		pmSetAttenDirect(atten);
	}
}

void PowerManager::pmStart()
{
	LOG(INFO);
	mRadio = gTRX->ARFCN(0);
	pmSetAttenDirect(gConfig.getNum("GSM.Radio.PowerManager.MaxAttenDB"));
}

}; // namespace GSM

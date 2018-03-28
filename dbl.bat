:Start
@echo off
color 0b
title Xaoni DBL API
echo Starting Xaoni DBL Counter
node --harmony dbl.js
echo.
echo -----------------------------------------------------------------------
echo (%time%) [WARNING]: DBL API Counter closed or crashed, restarting!
echo -----------------------------------------------------------------------
goto Start

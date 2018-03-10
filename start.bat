:Start
@echo off
color 0b
title Xaoni Discord Bot
echo Starting Xaoni
python bot.py
echo.
echo -------------------------------------------------------------
echo (%time%) [WARNING]: Xaoni closed or crashed, restarting!
echo -------------------------------------------------------------
goto Start

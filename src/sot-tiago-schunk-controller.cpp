/*
 * Copyright 2018,
 *
 * Joseph Mirabel
 *
 * LAAS, CNRS
 *
 * This file is part of TIAGOController.
 * TIAGOController is a free software, 
 *
 */

#include <sot/core/debug.hh>

/* TiagoSchunk is the instance of TIAGO named "schunk" */
#define ROBOTNAME std::string("TIAGOSCHUNK")

#include "sot-tiago-schunk-controller.hh"

const std::string SoTTiagoSchunkController::LOG_PYTHON_TIAGOSCHUNK="/tmp/TiagoSchunkController_python.out";

SoTTiagoSchunkController::SoTTiagoSchunkController():
  SoTTiagoController(ROBOTNAME)
{
  startupPython();
  interpreter_->startRosService ();
}

void SoTTiagoSchunkController::startupPython()
{
  SoTTiagoController::startupPython();
  std::ofstream aof(LOG_PYTHON_TIAGOSCHUNK.c_str());
  runPython
    (aof,
     "from dynamic_graph_sot_tiago.schunk.prologue import robot",
     *interpreter_);
  aof.close();
}

extern "C" 
{
  dgsot::AbstractSotExternalInterface * createSotExternalInterface()
  {
    return new SoTTiagoSchunkController;
  }
}

extern "C"
{
  void destroySotExternalInterface(dgsot::AbstractSotExternalInterface *p)
  {
    delete p;
  }
}

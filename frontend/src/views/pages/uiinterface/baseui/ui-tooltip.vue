<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Tooltip</h5>
        </div>
      </div>
      <div class="row">
        <!-- Tooltip -->
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Html Element</h5>
            </div>
            <div class="card-body">
              <div class="popover-list">
                <a-tooltip title="Popover title" placement="right">
                  <b-button variant="primary me-1"> Hover Me </b-button>
                </a-tooltip>
              </div>
            </div>
          </div>
        </div>
        <!-- /Tooltip -->

        <!-- Popover -->
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Direction Tooltip</h5>
            </div>
            <div class="card-body">
              <div class="tooltip-list">
                <a-tooltip title="Tooltip on top" placement="right">
                  <b-button variant="primary me-1"> Tooltip on top </b-button>
                </a-tooltip>
                <a-tooltip title="Tooltip on right" placement="right">
                  <b-button variant="primary me-1"> Tooltip on right </b-button>
                </a-tooltip>
                <a-tooltip title="Tooltip on bottom" placement="bottom">
                  <b-button variant="primary me-1"> Tooltip on bottom </b-button>
                </a-tooltip>
                <a-tooltip title="Tooltip on left" placement="left">
                  <b-button variant="primary me-1"> Tooltip on left </b-button>
                </a-tooltip>
              </div>
            </div>
          </div>
        </div>
        <!-- /Popover -->

        <!-- Tooltip -->
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Html Element</h5>
            </div>
            <div class="card-body">
              <div class="popover-list">
                <a-tooltip title="Tooltip with HTML" placement="right">
                  <b-button variant="primary me-1"> Tooltip with HTML </b-button>
                </a-tooltip>
                <a-tooltip title="Tooltip with HTML" placement="left">
                  <b-button variant="primary me-1"> Click Me </b-button>
                </a-tooltip>
              </div>
            </div>
          </div>
        </div>
        <!-- /Tooltip -->
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
import { Tooltip, Button } from "ant-design-vue";
export default {
  components: {
    "a-tooltip": Tooltip,
    "a-button": Button,
  },
  data() {
    return {
      title: "Tooltip",
    };
  },
};
</script>
<style>
:root {
  --popper-theme-background-color: #333333;
  --popper-theme-background-color-hover: #333333;
  --popper-theme-text-color: #ffffff;
  --popper-theme-border-width: 0px;
  --popper-theme-border-style: solid;
  --popper-theme-border-radius: 10px;
  --popper-theme-padding: 10px;
  --popper-theme-box-shadow: 0 6px 30px -6px rgba(0, 0, 0, 0.25);
}
</style>

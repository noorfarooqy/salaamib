<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="row">
        <div class="col-xl-3 col-md-4">
          <settingsidebar></settingsidebar>
        </div>

        <div class="col-xl-9 col-md-8">
          <div class="card">
            <div class="card-body two-factor w-100">
              <div class="content-page-header factor">
                <h5 class="setting-menu">Two-Factor Authentication Options</h5>
              </div>
              <div class="row">
                <div class="col-sm-9">
                  <div class="two-factor content p-0">
                    <h5>Text Message</h5>
                    <p>Use your mobile phone to receive security PIN.</p>
                  </div>
                </div>
                <div class="col-sm-3 text-end">
                  <div class="factor-checkbox">
                    <div class="status-toggle">
                      <input id="rating_1" class="check" type="checkbox" checked="" />
                      <label for="rating_1" class="checktoggle checkbox-bg factor">checkbox</label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="two-factor icon">
                <h5>
                  <img src="@/assets/img/two-factor-icon.svg" alt="Icon" /> Enabled, AUG
                  16, 2023
                </h5>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
};
</script>

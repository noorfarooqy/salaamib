<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="row">
        <div class="col-xl-3 col-md-4">
          <settingsidebar />
        </div>

        <div class="col-xl-9 col-md-8">
          <div class="card">
            <div class="card-body w-100">
              <div class="content-page-header">
                <h5>Preference Settings</h5>
              </div>
              <div class="row">
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <label>Currency</label>
                    <vue-select :options="Currency" id="currency" placeholder="Select Currency" />
                  </div>
                </div>
                <div class="col-lg-6 col-12">
                  <div class="input-block mb-3">
                    <label>Language</label>
                    <vue-select :options="Language" id="language" placeholder="Select Language" />
                  </div>
                </div>
                <div class="col-xl-6 col-lg-6 col-md-6 col-12">
                  <div class="input-block mb-3">
                    <label>Time Zone</label>
                    <vue-select :options="Time" id="zone" placeholder="Select Time Zone" />
                  </div>
                </div>
                <div class="col-xl-6 col-lg-6 col-md-6 col-12">
                  <div class="input-block mb-3">
                    <label>Date Format</label>
                    <vue-select :options="Dates" id="format" placeholder="Select Date Format" />
                  </div>
                </div>
                <div class="col-xl-6 col-lg-6 col-md-6 col-12">
                  <div class="input-block mb-3">
                    <label>Time Format</label>
                    <vue-select :options="Times" id="timeformat" placeholder="Select Time Format" />
                  </div>
                </div>
                <div class="col-xl-6 col-lg-6 col-md-6 col-12">
                  <div class="input-block mb-3">
                    <label>Financial Year </label>
                    <vue-select :options="Year" id="financialyear" placeholder="Select Financial Year" />
                  </div>
                </div>
                <div class="col-lg-12">
                  <div class="btn-path text-end">
                    <a href="javascript:void(0);" class="btn btn-cancel bg-primary-light me-3">Cancel</a>
                    <a href="javascript:void(0);" class="btn btn-primary">Save Changes</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  setup() {
    return {
      title: "Settings",
      Currency: [
        "USD - US Dollar",
        "GBP - British Pound",
        "EUR - Euro",
        "INR - Indian Rupee",
        "AUD - Australian Dollar",
      ],
      Language: ["English", "French", "German", "Italian", "Spanish"],
      Time: ["Select Time Zone", "10:00 AM - 11:00 AM", "12:00 PM - 02:00 PM"],
      Dates: ["Select Date Format", "2020 Nov 09", "09 Nov 2020", "09/11/2020"],
      Times: ["Select Time Format", "10:00 AM - 11:00 AM", "12:00 PM - 02:00 PM"],
      Year: [
        "Select Financial Year",
        "january-december",
        "february-january",
        "march-february",
      ],
    };
  },
};
</script>

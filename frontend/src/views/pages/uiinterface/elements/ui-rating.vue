<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>

    <!-- Page Wrapper -->
    <div class="page-wrapper">
      <div class="content container-fluid">
        <element-breadcrumb :title="title" />
        <div class="row">
          <!-- Rating -->
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <h5 class="card-title">Default Rating</h5>
              </div>
              <div class="card-body card-buttons">
                <p>This is the most basic example of ratings.</p>
                <star-rating v-bind:star-size="20" v-bind:show-rating="false" />
              </div>
            </div>
          </div>
          <!-- /Rating -->

          <!-- Rating -->
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <h5 class="card-title">Score</h5>
              </div>
              <div class="card-body card-buttons">
                <p>Stars with a saved rating.</p>
                <star-rating
                  v-bind:star-size="20"
                  v-bind:rating="3"
                  v-bind:show-rating="false"
                />
              </div>
            </div>
          </div>
          <!-- /Rating -->

          <!-- Rating -->
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <h5 class="card-title">Max Number</h5>
              </div>
              <div class="card-body card-buttons">
                <p>Change the max numbers of stars</p>
                <star-rating
                  v-bind:star-size="20"
                  v-bind:max-rating="10"
                  v-bind:show-rating="false"
                />
              </div>
            </div>
          </div>
          <!-- /Rating -->

          <!-- Rating -->
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <h5 class="card-title">Read Only</h5>
              </div>
              <div class="card-body card-buttons">
                <p>Prevent users from voting</p>
                <star-rating
                  v-bind:star-size="20"
                  v-bind:read-only="true"
                  v-bind:rating="3"
                  v-bind:show-rating="false"
                />
              </div>
            </div>
          </div>
          <!-- /Rating -->

          <!-- Rating -->
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <h5 class="card-title">Half Rating</h5>
              </div>
              <div class="card-body card-buttons">
                <p>You can represent a float score as a half star icon.</p>
                <star-rating
                  v-bind:star-size="20"
                  v-bind:increment="0.5"
                  v-bind:rating="3.5"
                  v-bind:show-rating="false"
                />
              </div>
            </div>
          </div>
          <!-- /Rating -->

          <!-- Rating -->
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <h5 class="card-title">Custom Icon</h5>
              </div>
              <div class="card-body card-buttons">
                <p>Use any icon you want.</p>
                <star-rating v-bind:star-size="20" v-bind:show-rating="false" />
              </div>
            </div>
          </div>
          <!-- /Rating -->
        </div>
      </div>
    </div>
    <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      title: "Rating",
      createElement: false,
    };
  },
};
</script>
